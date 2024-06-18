import subprocess
import json

# Function to run a TPM2 tool command
def run_tpm2_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

# Retrieve TCG Event Logs
def get_tcg_event_logs():
    command = ['tpm2_eventlog', '/sys/kernel/security/tpm0/binary_bios_measurements']
    output = run_tpm2_command(command)
    return output

# Retrieve PCR values
def get_pcr_values():
    command = ['tpm2_pcrread', '-Q', '-o', 'pcr_values.json']
    run_tpm2_command(command)
    with open('pcr_values.json') as f:
        pcr_values = json.load(f)
    return pcr_values

# Retrieve TPM Quote
def get_quote(pcr_list, key_handle):
    pcr_selection = ','.join([str(pcr) for pcr in pcr_list])
    command = ['tpm2_quote', '-c', key_handle, '-l', pcr_selection, '-m', 'quote_msg', '-s', 'quote_sig']
    run_tpm2_command(command)
    with open('quote_msg', 'r') as f:
        quote_msg = f.read()
    with open('quote_sig', 'r') as f:
        quote_sig = f.read()
    return quote_msg, quote_sig

# Get evidence
tcg_event_logs = get_tcg_event_logs()
pcr_values = get_pcr_values()
quote_msg, quote_sig = get_quote([0, 1, 2], '0x81000001')  # Example key handle


import hashlib

# Function to parse TCG Event Logs
def parse_event_logs(event_logs):
    # Simplified example: parse the logs and return a list of event measurements
    events = []
    for line in event_logs.splitlines():
        if "PCRIndex" in line and "Digest" in line:
            pcr_index = int(line.split('PCRIndex:')[1].split()[0])
            digest = line.split('Digest:')[1].strip()
            events.append((pcr_index, digest))
    return events

# Replay event logs and compare with PCR values
def replay_event_logs(event_logs, pcr_values):
    parsed_events = parse_event_logs(event_logs)
    for pcr_index, digest in parsed_events:
        pcr_value = pcr_values['pcrs'][str(pcr_index)]['value']
        if digest != pcr_value:
            print(f"Mismatch at PCR {pcr_index}: Event log digest {digest} != PCR value {pcr_value}")
        else:
            print(f"Match at PCR {pcr_index}: {digest}")

parsed_event_logs = parse_event_logs(tcg_event_logs)
replay_event_logs(tcg_event_logs, pcr_values)

# Function to measure data and extend into PCR
def extend_pcr_with_data(data, pcr_index):
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    command = ['tpm2_pcrextend', f'0:{pcr_index}:{data_hash}']
    run_tpm2_command(command)

# Example of extending a model's hash into PCR 15
model_data = "model data"
extend_pcr_with_data(model_data, 15)




import requests
import base64

# Function to send evidence to key server and get encrypted wrapper key
def get_encrypted_wrapper_key(server_url, evidence):
    response = requests.post(server_url, json=evidence, verify=True)
    response.raise_for_status()
    return response.json()['encrypted_wrapper_key']

# Function to decrypt the encrypted wrapper key within TEE
def decrypt_wrapper_key(encrypted_key, key_handle):
    decoded_key = base64.b64decode(encrypted_key)
    command = ['tpm2_rsadecrypt', '-c', key_handle, '-o', 'decrypted_key', '-m', decoded_key]
    run_tpm2_command(command)
    with open('decrypted_key', 'rb') as f:
        decrypted_key = f.read()
    return decrypted_key

# Example server URL and evidence data
server_url = "https://keyserver.example.com/get_key"
evidence = {
    "tcg_event_logs": tcg_event_logs,
    "pcr_values": pcr_values,
    "quote_msg": quote_msg,
    "quote_sig": quote_sig
}

# Get encrypted wrapper key
encrypted_wrapper_key = get_encrypted_wrapper_key(server_url, evidence)

# Decrypt the wrapper key using TPM (example key handle)
decrypted_wrapper_key = decrypt_wrapper_key(encrypted_wrapper_key, '0x81000001')

# Use the decrypted key to decrypt the model/data (implementation depends on the encryption method used)
