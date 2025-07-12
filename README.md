# Ecommerce Project.
Developed with:
1. Python 3.13.3
2. Django
3. HTML and CSS

# Installation steps.
1. Clone the repository and navigate to the project.
```bash
git clone https://github.com/David-Peralta-Rd/Proyecto-Ecommerce-Para-Trabajo-Sena.git
cd Proyecto-Ecommerce-Para-Trabajo-Sena
```
2. Create and activate the virtual environment.
```bash
# Create environment (Windows/Linux/Mac)
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```
3. Install dependencies and activate project changes.
```bash
# Install dependencies.
pip install -r requirements.txt

# Activate changes to the database.
python manage.py makemigrations

# Migrate models to the database.
python manage.py migrate
```
4. Finally, we'll activate our project and create an admin user:
```bash
# Activate the project on port 8000 or any other port
python manage.py runserver

# If you want to activate it on another port, type:
python manage.py runserver 3000 # It can be any port; in my case, I used 3000.

# Create the admin user. Fill in the details, and you'll have a super user.
python manage.py createsuperuser
```
# Access the locally mounted website:
http://localhost:8000/

# Log in as admin
http://localhost:8000/admin/

# Testing my work for the project:
1. Home:

![image](https://github.com/user-attachments/assets/88c6c194-5f6a-4854-9bc9-917fb624a98f)

2. In the categories:

![image](https://github.com/user-attachments/assets/e82f3985-2333-4358-8cf8-795ec8ff49d4)

3. Menu buys:

![image](https://github.com/user-attachments/assets/1940954d-271d-4d5e-83f5-644e2369273e)

4. Accept purchase:

![image](https://github.com/user-attachments/assets/bcf6350f-c3d4-447d-a1c2-f060a36ca091)

5. Confirmed Purchase:

![image](https://github.com/user-attachments/assets/5054457a-edab-4d12-aab2-79e6f403850c)

6. Menu admin:

![image](https://github.com/user-attachments/assets/881742d4-c1ad-4fc6-9bd4-bf3024ae5fd8)

# Use the Draw.io integration extension to view the general diagram, image:
![image](https://github.com/user-attachments/assets/b373f600-a04a-466c-8d14-afd2fa0af138)

# End
This would be my project for a SENA project. I clarify that this is a project that I do not guarantee its serious use.
It's simple and to the point.

LICENSE: Mit

@Created by David Peralta✌️.
