# JSON structure for media

Note: Some field types may be incorrect, this exists just to get a gist of the structure.

```json
{
  "media": {
    "taken_at": "integer",
    "pk": "string",
    "id": "string",
    "device_timestamp": "integer",
    "client_cache_key": "string",
    "filter_type": "integer",
    "caption_is_edited": "boolean",
    "like_and_view_counts_disabled": "boolean",
    "is_reshare_of_text_post_app_media_in_ig": "boolean",
    "media_type": "integer",
    "code": "string",
    "can_viewer_reshare": "boolean",
    "caption": {
      "pk": "string",
      "user_id": "string",
      "text": "string",
      "type": "integer",
      "created_at": "integer",
      "created_at_utc": "integer",
      "content_type": "string",
      "status": "string",
      "bit_flags": "integer",
      "did_report_as_spam": "boolean",
      "share_enabled": "boolean",
      "user": {
        "has_anonymous_profile_picture": "boolean",
        "fan_club_info": {
          "fan_club_id": "null",
          "fan_club_name": "null",
          "is_fan_club_referral_eligible": "null",
          "fan_consideration_page_revamp_eligibility": "null",
          "is_fan_club_gifting_eligible": "null",
          "subscriber_count": "null",
          "connected_member_count": "null",
          "autosave_to_exclusive_highlight": "null",
          "has_enough_subscribers_for_ssc": "null"
        },
        "fbid_v2": "string",
        "transparency_product_enabled": "boolean",
        "hd_profile_pic_url_info": {
          "url": "string",
          "width": "integer",
          "height": "integer"
        },
        "hd_profile_pic_versions": [
          {
            "width": "integer",
            "height": "integer",
            "url": "string"
          }
        ],
        "is_favorite": "boolean",
        "is_unpublished": "boolean",
        "text_post_app_joiner_number": "integer",
        "pk": "string",
        "pk_id": "string",
        "username": "string",
        "full_name": "string",
        "is_private": "boolean",
        "is_verified": "boolean",
        "friendship_status": {
          "following": "boolean",
          "outgoing_request": "boolean",
          "is_bestie": "boolean",
          "is_restricted": "boolean",
          "is_feed_favorite": "boolean"
        },
        "profile_pic_id": "string",
        "profile_pic_url": "string",
        "account_badges": [],
        "feed_post_reshare_disabled": "boolean",
        "show_account_transparency_details": "boolean",
        "third_party_downloads_enabled": "integer",
        "latest_reel_media": "integer"
      },
      "is_covered": "boolean",
      "is_ranked_comment": "boolean",
      "media_id": "string",
      "has_translation": "boolean",
      "private_reply_status": "integer"
    },
    "clips_tab_pinned_user_ids": [],
    "comment_inform_treatment": {
      "should_have_inform_treatment": "boolean",
      "text": "string",
      "url": "null",
      "action_type": "null"
    },
    "has_viewer_saved": "boolean",
    "saved_collection_ids": [],
    "sharing_friction_info": {
      "should_have_sharing_friction": "boolean",
      "bloks_app_url": "null",
      "sharing_friction_payload": "null"
    },
    "accessibility_caption": "string",
    "original_media_has_visual_reply_media": "boolean",
    "can_viewer_save": "boolean",
    "is_in_profile_grid": "boolean",
    "profile_grid_control_enabled": "boolean",
    "featured_products": [],
    "is_comments_gif_composer_enabled": "boolean",
    "product_suggestions": [],
    "user": {
      "has_anonymous_profile_picture": "boolean",
      "fan_club_info": {
        "fan_club_id": "null",
        "fan_club_name": "null",
        "is_fan_club_referral_eligible": "null",
        "fan_consideration_page_revamp_eligibility": "null",
        "is_fan_club_gifting_eligible": "null",
        "subscriber_count": "null",
        "connected_member_count": "null",
        "autosave_to_exclusive_highlight": "null",
        "has_enough_subscribers_for_ssc": "null"
      },
      "fbid_v2": "string",
      "transparency_product_enabled": "boolean",
      "hd_profile_pic_url_info": {
        "url": "string",
        "width": "integer",
        "height": "integer"
      },
      "hd_profile_pic_versions": [
        {
          "width": "integer",
          "height": "integer",
          "url": "string"
        }
      ],
      "is_favorite": "boolean",
      "is_unpublished": "boolean",
      "text_post_app_joiner_number": "integer",
      "pk": "string",
      "pk_id": "string",
      "username": "string",
      "full_name": "string",
      "is_private": "boolean",
      "is_verified": "boolean",
      "friendship_status": {
        "following": "boolean",
        "outgoing_request": "boolean",
        "is_bestie": "boolean",
        "is_restricted": "boolean",
        "is_feed_favorite": "boolean"
      },
      "profile_pic_id": "string",
      "profile_pic_url": "string",
      "account_badges": [],
      "feed_post_reshare_disabled": "boolean",
      "show_account_transparency_details": "boolean",
      "third_party_downloads_enabled": "integer",
      "latest_reel_media": "integer"
    },
    "image_versions2": {
      "candidates": [
        {
          "width": "integer",
          "height": "integer",
          "url": "string"
        }
      ]
    },
    "original_width": "integer",
    "original_height": "integer",
    "max_num_visible_preview_comments": "integer",
    "has_more_comments": "boolean",
    "comment_threading_enabled": "boolean",
    "preview_comments": [],
    "comments": [],
    "comment_count": "integer",
    "can_view_more_preview_comments": "boolean",
    "hide_view_all_comment_entrypoint": "boolean",
    "inline_composer_display_condition": "string",
    "has_liked": "boolean",
    "like_count": "integer",
    "shop_routing_user_id": "null",
    "can_see_insights_as_brand": "boolean",
    "is_organic_product_tagging_eligible": "boolean",
    "music_metadata": {
      "music_canonical_id": "string",
      "audio_type": "string",
      "start_time_in_video_in_ms": "integer",
      "end_time_in_video_in_ms": "integer",
      "should_mute_audio": "boolean",
      "should_auto_play_audio": "boolean",
      "song_id": "string",
      "product_id": "string",
      "display_artist": "string",
      "display_title": "string",
      "cover_artwork_uri": "string",
      "large_cover_artwork_uri": "string",
      "apple_music_id": "string",
      "spotify_track_id": "string",
      "spotify_album_id": "string",
      "amazon_product_url": "string"
    },
    "deleted_reason": "integer",
    "integrity_review_decision": "string",
    "has_shared_to_fb": "integer",
    "is_unified_video": "boolean",
    "should_request_ads": "boolean",
    "is_visual_reply_commenter_notice_enabled": "boolean",
    "commerciality_status": "string",
    "explore_hide_comments": "boolean",
    "product_type": "string",
    "is_paid_partnership": "boolean",
    "organic_tracking_token": "string",
    "ig_media_sharing_disabled": "boolean",
    "has_delayed_metadata": "boolean"
  }
}
```