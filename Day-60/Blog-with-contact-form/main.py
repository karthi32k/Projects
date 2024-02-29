from flask import Flask, render_template, request
import requests
import smtplib
import datetime

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/a0a1aacad84685221725").json()

FROM_EMAIL = "fibonaccicoder@gmail.com"
PASSWORD = "ysbgmsatyhfaddam"
TO_EMAIL = "fibonaccicoder@gmail.com"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        # print(data["name"])
        # print(data["email"])
        # print(data["phone"])
        # print(data["message"])
        # return "<h1>Successfully sent your message</h1>"
        return render_template("contact.html", msg_send=True)
    return render_template("contact.html", msg_send=False)


# Send the mail to a receiver message
def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=150) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(TO_EMAIL, TO_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
