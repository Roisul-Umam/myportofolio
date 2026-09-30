def navigation(request):
    return {
        "navigation_links": [
            {"name": "Profile", "url_name": "main:show_main"},
            {"name": "Experience", "url_name": "main:show_experience"},
            {"name": "Projects", "url_name": "main:show_projects"},
        ],
        "short_name": "Rois",
    }