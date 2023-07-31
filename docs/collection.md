# JSON structure for 

Note: Some field types may be incorrect, this exists just to get a gist of the structure.

```json
{
  "items": [
    {
      "collection_id": "ALL_MEDIA_AUTO_COLLECTION",
      "collection_name": "All Posts",
      "collection_type": "ALL_MEDIA_AUTO_COLLECTION",
      "collection_media_count": -1,
      "cover_media_list": [
          {
            "id": "",
            "media_type": 1,
            "image_versions2": {
              "candidates": [
                {
                  "width": -1,
                  "height": -1,
                  "url": ""
                }
              ]
            },
            "original_width": -1,
            "original_height": -1,
            "explore_pivot_grid": false,
            "accessibility_caption": "",
            "product_type": ""
          },
        ...
      ]
    },
    {
      "collection_id": "",
      "collection_name": "Collection #1",
      "collection_type": "MEDIA",
      "cover_media": {
        "id": "",
        "media_type": 1,
        "image_versions2": {
          "candidates": []
        },
        "original_width": -1,
        "original_height": -1,
        "explore_pivot_grid": false,
        "accessibility_caption": "",
        "product_type": ""
      },
      "cover_media_list": [],
      "collection_media_count": -1,
      "viewer_access_level": "write"
    },
    ...
  ],
  "more_available": false,
  "auto_load_more_enabled": true,
  "status": "ok"
}
```