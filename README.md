

---

# 📚 Smart Study Group Finder

A Django-based web application that helps students find and join study groups tailored to their interests, preferences, and subjects. Think of it as a smart matchmaking platform for collaborative learning.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Sign up, log in, and manage personal profiles.
  
- 📄 **Personalized Profiles**
  - Select subjects of interest.
  - Choose group preferences (Public / Private / All).
  
- 🎯 **Group Matching (Tinder-style)**
  - Instantly matched with study groups based on your preferences.
  - Explore and discover new groups using custom filters.

- 👥 **Group Access Control**
  - **Public Groups**: Instant join access.
  - **Private Groups**: Join only after admin approval.
  
- 💬 **Real-time Group Chat**
  - Channel-based communication using Django Channels (WebSockets).
  - Share study material, notes, and resources within each group.
  
- 🛠️ **Group Creation**
  - Create your own study group based on one or more subjects.
  - Choose between public or private group types and manage members.

---

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Real-time Communication**: Django Channels (WebSockets)
- **Frontend**: HTML, CSS, JavaScript (Django templates or frontend framework)
- **Database**: SQLite (`db.sqlite3`)

---

## 📂 Project Structure

```

Study-Group-Finder/
├── accounts/         # User registration, login, profiles
├── groups/           # Group creation, discovery, join requests
├── chat/             # Real-time messaging via channels
├── templates/        # HTML UI templates
├── static/           # CSS and JavaScript files
├── media/            # Uploaded files and shared resources
├── db.sqlite3        # SQLite database
├── manage.py
└── requirements.txt

````


🧪 Getting Started (Local Development)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vis89-svg/Study-Group-Finder.git
   cd Study-Group-Finder
---

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Open your browser and go to:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🙋‍♂️ Contributions

Contributions, issues, and feature suggestions are welcome!
Feel free to open a pull request or submit an issue.

---

Let me know if you want:
- A `requirements.txt` template
- `.gitignore` for Django projects
- Sample environment variable `.env` template

Happy coding! 🚀
```
