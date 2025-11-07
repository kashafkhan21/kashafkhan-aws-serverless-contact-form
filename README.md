# AWS serverless contact form

Project Goal:
To build a highly reliable, zero-maintenance contact form backend using only AWS Serverless services. This demonstrates competence in building cost-effective, modern cloud solutions.

🚀 Live Demo
Live Website: https://kashafkhan21.github.io/kashafkhan-aws-serverless-contact-form/

🛠 Architecture Overview
This system is composed of four main serverless components working together:
1.  AWS S3 (Frontend): Hosts the static HTML webpage.
2.  AWS API Gateway (HTTP API): Acts as the secure entry point for the contact form data.
3.  AWS Lambda (Python): The core business logic. It processes the incoming request and generates a unique ID for the submission.
4.  Amazon DynamoDB: Stores all messages persistently in a NoSQL database table.
|
✅ Proof of Work
 1. Successful Client Submission
(Shows the form running live and successfully receiving a 200 response from the API.)

 2. Database Persistence
(Shows the final proof: the message is saved in the NoSQL database.)

👨‍💻 Get the Code
The core logic for saving data is contained in:
* contact.html (Frontend code and JavaScript submission logic)
* lambda_function.py (Python backend logic)
