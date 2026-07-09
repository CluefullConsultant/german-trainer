# pronunciation.py
import streamlit as st
import boto3


def _client():
    return boto3.client(
        "polly",
        aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
        region_name=st.secrets.get("AWS_REGION", "eu-central-1"),
    )


@st.cache_data(ttl=None, show_spinner=False)
def synthesize_speech(text: str) -> bytes:
    """German audio (MP3 bytes) for the given text via Amazon Polly's neural voice."""
    client = _client()
    response = client.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Vicki",
        Engine="neural",
        LanguageCode="de-DE",
    )
    return response["AudioStream"].read()
