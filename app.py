import streamlit as st
import pandas as pd
import json
import base64
import io
from PIL import Image

# This sets the page title and a cute favicon
st.set_page_config(page_title="Squirrel Census", page_icon="🐿")

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df = df.fillna("None")
    return df

data = load_data("data/squirrel_census.csv")

st.title("The Central Park Squirrel Census🐿")
st.image("data/central_park.jpg")
st.markdown(
    """As part of the [Squirrel Census](https://www.thesquirrelcensus.com/) in 2018, 
     volunteers counted all squirrels in Central Park and recorded features like their
     color, where they were sighted and whether they were doing anything interesting at
     that time. Strangely, this was the first time anyone had ever attempted anything 
     like this. The results? Central Park is the home of **3023 squirrels**, most of 
     which are gray! A few of them must be especially fast, since the Census volunteers 
     weren't even able to see what color they had 🐿💨"""
)

# Add a divider with custom style
st.markdown("""
    <hr style="
        height: 2px;
        background-color: #444;
        border: none;
        margin: 20px 0;
    ">
""", unsafe_allow_html=True)

# Load blog posts from JSON file
def load_blog_posts():
    try:
        with open("blog_posts.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"text_posts": [], "image_posts": []}


# Initialize session state to store blog posts
if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = load_blog_posts()

# Initialize session state to store blog posts
if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = {"text_posts": [], "image_posts": []}

# Function to add a new text-based blog post
def add_text_post():
    title = st.text_input("Post Title")
    content = st.text_area("Post Content")
    if st.button("Submit Text Post"):
        st.session_state.blog_posts["text_posts"].append({"title": title, "content": content})
        save_blog_posts(st.session_state.blog_posts)
        st.success("Text post added!")
        st.rerun()  # Rerun the app to display the updated list of posts

# Function to add a new image-based blog post
def add_image_post():
    title = st.text_input("Image Title")
    message = st.text_area("Image Message")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image_data = uploaded_file.read()  # Read the image file as binary bytes
        if st.button("Submit Image Post"):
            # Encode image data to Base64 ASCII string
            encoded_image_data = base64.b64encode(image_data).decode('ascii')
            # Store the image as a Base64 string in the blog post
            st.session_state.blog_posts["image_posts"].append({
                "title": title,
                "message": message,
                "image": encoded_image_data  # Store the encoded image data
            })
            save_blog_posts(st.session_state.blog_posts)
            st.success("Image post added!")
            st.rerun()  # Rerun the app to display the updated list of posts

# Save blog posts to JSON file
def save_blog_posts(posts):
    with open("blog_posts.json", "w") as f:
        # Use custom serialization function to handle bytes
        json.dump(posts, f, default=serialize)

# Custom serialization function to handle bytes
def serialize(obj):
    if isinstance(obj, bytes):
        # Convert bytes to ASCII string
        return obj.decode('ascii')
    raise TypeError("Type not serializable")
            

# Display the form for adding a new text-based blog post
st.header("Create a New Text Post")
add_text_post()

# Display the form for adding a new image-based blog post
st.header("Create a New Image Post")
add_image_post()

# Display all existing blog posts
st.header("Blog Posts")

# Display text-based blog posts
st.subheader("Text Posts")
if "text_posts" in st.session_state.blog_posts:
    for post in st.session_state.blog_posts["text_posts"]:
        st.subheader(post["title"])
        st.write(post["content"])
        st.markdown("---")  # Add a divider between posts
else:
    st.write("No text posts available.")

# Display image-based blog posts
st.subheader("Image Posts")
if "image_posts" in st.session_state.blog_posts:
    for post in st.session_state.blog_posts["image_posts"]:
        st.subheader(post["title"])
        st.write(post["message"])
        st.image(base64.b64decode(post["image"]), use_column_width=True)
        st.markdown("---")  # Add a divider between posts
else:
    st.write("No image posts available.")