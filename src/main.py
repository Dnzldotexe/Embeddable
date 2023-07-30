"""
This app converts the normal google drive links to an embeddable link for HTML
"""
# Importing pyperclip clipboard module
import pyperclip as clip

# Importing streamlit third-party App Framework
import streamlit as st


# Setting the page Title and Icon
st.set_page_config(page_title="Embeddable", page_icon="📎")


def link_convert(link: str):
    """
    Replaces the links' prefixes and suffixes to be embeddable
    """
    # If https is present
    if "https" in link:
        # Replaces ordinary prefix with embeddable prefix
        link = link.replace(
            "https://drive.google.com/file/d/",
            "https://drive.google.com/uc?export=view&id="
        )

    # If drive_link is present
    if "drive_link" in link:
        # Removes the ordinary suffix
        link = link.replace("/view?usp=drive_link", "")

    # If view is present
    if "view" in link:
        # Removes the ordinary suffix
        link = link.replace("/view", "")

    # Returns the embeddable link
    return link


def main():
    """
    Contains the main application
    """
    # Adding title
    st.title("📋 Google Drive Link Converter")

    # Adding text area input
    url_input = st.text_area(label=" ",placeholder="paste your google drive links here")

    # Additional information
    st.info("Links are automatically converted, just press the Copy button")

    # Stores the converted link
    converted_url = link_convert(url_input)

    # Copy to clipboard button
    if st.button("Copy"):
        clip.copy(converted_url)
        st.success("Link/s copied to clipboard!")


# Running main
if __name__ == "__main__":
    main()
