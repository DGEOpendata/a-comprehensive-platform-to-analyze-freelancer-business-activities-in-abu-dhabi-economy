markdown
# Freelancer Business Activities Dataset API

This project provides a Flask-based API for accessing and searching the Freelancer Business Activities Dataset for Abu Dhabi.

## Features
- Retrieve all freelancer business activities.
- Search freelancer business activities by keywords in English or Arabic.
- Access data in a user-friendly JSON format.

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Installation
1. Clone the repository:
    bash
    git clone https://github.com/username/freelancer-business-activities-api.git
    cd freelancer-business-activities-api
    
2. Install required dependencies:
    bash
    pip install -r requirements.txt
    
3. Place the dataset file (`Freelancer_Business_Activities_AbuDhabi.xlsx`) in the project root directory.

## Usage
1. Run the Flask application:
    bash
    python app.py
    
2. Access the API at `http://127.0.0.1:5000`

### Endpoints
#### 1. Get All Freelancer Activities
- **URL**: `/api/freelancers`
- **Method**: GET
- **Description**: Retrieves all freelancer business activities.
- **Response**:
  
  [
    {
      "Activity ID": "123",
      "English Name": "Cooking Consultancy",
      "Arabic Name": "استشارات الطهي"
    },
    ...
  ]
  

#### 2. Search Freelancer Activities
- **URL**: `/api/freelancers/search`
- **Method**: GET
- **Query Parameter**: `q` (string) - The keyword to search for.
- **Description**: Searches for freelancer activities by keyword (in both English and Arabic).
- **Response**:
  
  [
    {
      "Activity ID": "125",
      "English Name": "Sports Event Marketing",
      "Arabic Name": "تسويق الأحداث الرياضية"
    },
    ...
  ]
  

## Contributing
1. Fork the repository.
2. Create a new branch:
    bash
    git checkout -b feature/your-feature-name
    
3. Make your changes and commit them:
    bash
    git commit -m "Add your message here"
    
4. Push to the branch:
    bash
    git push origin feature/your-feature-name
    
5. Submit a pull request.

## License
This project is licensed under the MIT License.
