import enum
from urllib.parse import urlparse
from os import path


class MediaType(enum.IntFlag):
    # This is obscure for no reason (:
    PHOTO       = 1 << 0
    VIDEO       = 1 << 1
    CAROUSEL    = 1 << 3
    IGTV        = 1 << 5
    REEL        = 1 << 6


IMGV = "image_versions2"
VIDV = "video_versions"
CMED = "carousel_media"


class Post:
    
    def __init__(self):
        self.epoch = -1
        self.code = ""
        self.type = -1
        self.poster = ""
        self.candidates = []

    def to_dict(self):
        return {
            "code": self.code,
            "epoch": self.epoch,
            "type": self.type,
            "poster": self.poster,
            "candidates": self.candidates}
    
    def get_filenames(self):
        filenames = []

        for i, url in enumerate(self.get_urls()):
            ext = parse_url_extension(url)
            
            filename = f"{self.code}_{self.poster}_{i}_{self.epoch}{ext}"
            filenames.append(filename)

        return filenames

    def get_urls(self):
        # Return the highest resolution candidate
        if self.type == MediaType.CAROUSEL:
            return [s[0].get("url") for s in self.candidates]
        
        # Return highest resolution candidate for other
        return [self.candidates[0].get("url")]
    
    def __str__(self):
        return f"Post(code={self.code}, type={self.type}, poster=\"{self.poster}\")"

def parse_url_extension(url: str):
    base_p = path.basename(urlparse(url).path)
    _, ext = path.splitext(base_p)

    return ext

def parse_media(media: dict):
    p = Post()

    p.epoch = media.get("taken_at", -1)
    p.code = media.get("code")
    p.type = media.get("media_type")
    p.poster = media.get("user", {}).get("username")
    p.candidates = _detect_media_candidates(media)
    
    return p


def _parse_carousel(carousel: list):
    media = []

    for c in carousel:
        candidates = _detect_media_candidates(c)
        media.append(candidates)

    assert len(media) == len(carousel)

    return media


def _detect_media_candidates(media):
    candidates = []

    match (m_type := media.get("media_type")):
        case MediaType.PHOTO:
            candidates = media.get(IMGV).get("candidates")

        case MediaType.VIDEO:
            candidates = media.get(VIDV)

        # tfw python cases can't fall through x1
        case MediaType.REEL:
            candidates = media.get(VIDV)

        # tfw python cases can't fall through x2
        case MediaType.IGTV:
            candidates = media.get(VIDV)

        case MediaType.CAROUSEL:
            candidates = _parse_carousel(media.get(CMED))

        case _:
            raise NotImplementedError(f"Unknown media type: `{m_type}`")

    return candidates
