# Unai Gómez-Hernández’s academic website

Personal academic website: https://unaigomezhernandez.github.io

Minimal Jekyll site, based on the Kiko theme and Titipat Achakulvisut’s personal website. Existing colours, fonts, page URLs, contact details, publication links, and CV PDF are retained.

## Local preview and validation

Use Ruby 3.1+ and Bundler:

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
bundle exec jekyll serve
```

Open http://127.0.0.1:4000. Check navigation, keyboard focus, zoom, and layout at mobile and desktop widths. The dependency manifest targets the Jekyll 3.x build used by GitHub Pages; no additional Pages plugin is required. Do not deploy or merge a profile update until its owner approves it.

## Content maintenance

- Home introduces the profile; About covers education and experience; Research describes interests and methods.
- Current roles and PhD completion were supplied by the owner for October 2026. No role start dates or projects have been inferred.
- Publications contain 25 entries grouped by type. Five entries were added from the September 2026 CV, with verified links where a public source was available. The Europe-Asia Studies item is a book review, not a research article. The SICSS blog entry’s publication year is corrected to 2025 (the event was in 2024), supported by the [University of Edinburgh’s notice](https://www.cdcs.ed.ac.uk/all/news/2025-03/trip-barcelona-summer-institute-computational-social-sciences). FEPS identifies the participation papers as policy studies.
- Unpublished reports and library-archived research remain under Other research; no peer-review status is inferred.
- The Global Policy title, volume, supplement, and page range are corrected against the [publisher’s citation](https://onlinelibrary.wiley.com/doi/10.1111/1758-5899.13414). Existing citation details otherwise remain unchanged; this update does not claim a complete bibliography through October 2026.
- The September 2026 CV was used to audit the website. The public CV download remains unchanged unless the owner explicitly approves publishing the supplied PDF, which contains named referees and contact details. Website facts explicitly supplied by the owner, including the June 2026 PhD completion and Guest Professor role, remain authoritative where the CV uses older or less complete wording.
- `_posts` contains inherited theme demonstration content about a different person. It is excluded from the site and feed, but retained in Git. Those old demo URLs will return the existing 404 page after an approved deployment.
- The footer disclaimer is maintained in the shared default layout.
