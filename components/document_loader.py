from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# ──────────────────────────────────────────────
# Stage 1a — Document Ingestion
# ──────────────────────────────────────────────

# Supported language codes and display labels
SUPPORTED_LANGUAGES = {
    "English": ["en"],
    "Hindi": ["hi"],
    "Hindi (Auto-generated)": ["hi", "en"],
    "English (Auto-generated)": ["en", "hi"],
}


def load_transcript(video_id: str, language: str = "English") -> str | None:
    """
    Fetch the transcript of a YouTube video in the selected language.

    Args:
        video_id: The YouTube video ID (not the full URL).
        language: Display label from SUPPORTED_LANGUAGES (default: "English").

    Returns:
        Plain text transcript string, or None if unavailable.

    Raises:
        RuntimeError: If an unexpected error occurs during fetching.
    """
    lang_codes = SUPPORTED_LANGUAGES.get(language, ["en"])

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=lang_codes)
        transcript = " ".join(snippet.text for snippet in fetched)
        return transcript
    except TranscriptsDisabled:
        return None
    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: {e}") from e
