from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# ──────────────────────────────────────────────
# Stage 1a — Document Ingestion
# ──────────────────────────────────────────────

def load_transcript(video_id: str) -> str | None:
    """
    Fetch the English transcript of a YouTube video.

    Args:
        video_id: The YouTube video ID (not the full URL).

    Returns:
        Plain text transcript string, or None if unavailable.

    Raises:
        RuntimeError: If an unexpected error occurs during fetching.
    """
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=["en"])
        transcript = " ".join(snippet.text for snippet in fetched)
        return transcript
    except TranscriptsDisabled:
        return None
    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: {e}") from e
