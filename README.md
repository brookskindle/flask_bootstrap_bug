# What?
This project is a simple proof of concept to demonstrate pagination in flask
bootstrap.

Actually, it's meant to show that the pagination portion of `flask_bootstrap`
up to `3.3.7.1.dev1` (what I'm testing this against) with jinja2 >= 2.9.3 is
not working.

This project is built using python3.

# How do I test this?

1. clone this repo (ala `git clone`)
1. `pip install -r requirements.txt`
1. Run the app
    * `python app.py`
1. Point your browser to `localhost:5000`

At this point, you should receive an error saying `url_args` is undefined

This is due to a change in jinja2 version `2.9.3` (not sure which, I didn't
write the changes)

If you want to see what this project *should* look like, reinstall an older
version of jinja2
```
pip install jinja2==2.9.2  # or lower
```
