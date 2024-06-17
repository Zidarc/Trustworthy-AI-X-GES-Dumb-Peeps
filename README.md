# Trustworthy AI Lab x GES UCLA Hackathon
## Enhancing CTR Predictions through a Data Clean Room

### ABOUT
The Global Entrepreneurship Society (GES) at UCLA, formerly known as Three Day Startup, is a highly competitive entrepreneurial education program designed for university students. Each year, around 40 enthusiastic future entrepreneurs are selected from over 120 applicants to develop their most brilliant ideas, refine business models, and deliver viable ventures in our learning-by-doing programs.

This year, GES is honored to hold a hackathon following the trend of generative AI. This event offers a unique experience to brainstorm startup ideas, develop sustainable business plans, showcase technical and communication skills, and engage with like-minded students.

### Overview
The main theme of this event is to utilize Generative AI to empower “Data Collaboration Intelligence.” Participating teams will develop a data-sharing platform that allows private data sharing, predictive analytics, and model building among different data parties. Specifically, each team will develop a “Data Clean Room” to enhance Click-through Rate (CTR) predictions using privacy-preserving synthetic data.

### Background
The Data Clean Room is a secure framework that facilitates data sharing between two distinct parties. In the CTR case, we have two parties:
- **Publishers (providing `train_data_feeds.csv`)**: They focus on user interactions with news content.
- **Advertisers (providing `train_data_ads.csv`)**: They concentrate on user interactions with advertisements.

This arrangement ensures that both parties can access broader datasets while maintaining user privacy and data security.

### Challenges
1. **Synthetic Data Fidelity**:
   - Create synthetic datasets that accurately reflect real-world distributions of user behavior data.
2. **Synthetic Data Utility**:
   - **Publishers**: Enhance predictive accuracy for user engagement with news content by integrating user interaction patterns from the advertisement dataset. This aims at better content personalization and placement strategies.
   - **Advertisers**: Refine prediction models for advertisements by using synthesized data from news content interactions to understand the most effective contexts for ad placements.

### Dataset Overview
1. **`train_data_ads.csv`**: Includes user demographics, device information, advertisement specifics, and user interaction data.
2. **`train_data_feeds.csv`**: Contains detailed device info, content engagement metrics, and user interaction labels.

### Data Clean Room Mechanics
- Construct a Data Clean Room (DCR) to train the CTR model within the DCR.
- Ensure datasets remain encrypted outside of the DCR to guarantee that only the DCR can decrypt the data.
- Multiple parties can collaborate on data synthesis by merging two datasets based on IDs. Only the data owner will have access to their specific data outside the DCR.

### Potential Technical Challenges
- **Synthetic Data Generation Accuracy**: Creating synthetic data that accurately represents the complex distributions of real-world data without inheriting biases.
- **Trust Execution Environment (TEE)**: Build or utilize a DCR and train the model within the TEE.
- **Integration of Heterogeneous Data Sources**: Merging data from different datasets (publisher and advertiser data) with varying structures and formats to ensure seamless data integration within the Data Clean Room.
- **Scalability and Real-Time Processing**: Developing scalable solutions capable of handling large datasets and processing data in real-time to provide timely and efficient insights.

### Expected Outcomes
- Development of more accurate predictive models for CTR that consider a richer set of anonymized data.
- Demonstration of effective collaboration within a privacy-preserving environment.
- Enhanced understanding of cross-party data utility without direct data exposure.

### Benefits to Participants
- Experience with real-world datasets and privacy-preserving technologies driven by generative AI.
- Insights into advanced data analytics and synthetic data applications in digital marketing and content distribution.

### Add-ons
- **Workshops**: Training sessions on generative AI, synthetic data generation, and data clean room technologies.
- **Mentorship**: Access to mentors from the tech industry and academia to guide participants through the hackathon.
- **Networking**: Opportunities to connect with like-minded peers, industry professionals, and potential investors.
- **Prizes**: Awards for the top-performing teams, including cash prizes, tech gadgets, and internship opportunities.

## Assessment Criteria
1. **Accuracy and Predictive Performance**:
   - Projects will be evaluated based on the accuracy and reliability of their predictive models. Higher precision in forecasting user engagement with news content and advertisements will be favored.
2. **Innovation and Creativity**:
   - Judges will assess the novelty and creativity of the solutions, especially in terms of how participants handle data integration, synthesis, and privacy-preserving techniques within the Data Clean Room.
3. **Scalability and Efficiency**:
   - The ability of the solution to scale efficiently with increasing data volumes and to process data in real-time will be crucial. Projects need to demonstrate performance stability and resource management.

## Submission
1. Runnable Data Clean Room code in a Github Repo.
2. CTR Prediction machine learning code in a Python package/script.
3. 3-5 page presentation slides, not including index and references.

## Team Name: Dumb Peeps

- **Ali Hussain**
- **Abbad Shahabi**
- **Ameen Abbasi**


---
