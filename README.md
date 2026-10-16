# Corpus updates

Public project updates for the ancient scripts corpus initiative.

## Publish the blog

In Settings → Pages, select **Deploy from a branch**, then **main** and **/(root)**, and save. GitHub builds this Jekyll site automatically.

Expected address: https://hawkinsnick.github.io/Corpus-updates/

## Add an update

Create `_posts/YYYY-MM-DD-short-title.md` with YAML front matter: layout: post, title: "Your title", date: 2026-10-12 12:00:00 -0500, categories: [project]. Template: `templates/update.md`.

Include what changed, validation, source and rights status, unresolved scholarly questions, and next steps. Link to exact commits or merged PRs for completed work. Describe branch-only work as pending.

This repository publishes editorial updates, not corpus data or AI skill bundles. Authoritative corpus documentation and individual/master AI skills remain in their respective repositories.

## Research discovery portal

The GitHub Pages site now offers a research homepage, [corpus directory](https://hawkinsnick.github.io/Corpus-updates/corpora/), [Linear A guide](https://hawkinsnick.github.io/Corpus-updates/linear-a/), updates, and contribution instructions. The source of truth for inscriptions and individual/master AI skills remains in the existing repositories; the portal does not duplicate or alter corpus records.

SEO implementation: shared page-specific title/description and canonical tags, Open Graph metadata, a Jekyll-generated `sitemap.xml`, and `robots.txt`. Verify the live Pages deployment before submitting the sitemap to Google Search Console. Google indexing is not guaranteed. Before adding new corpus pages, verify repository names, evidence scope, scholarly limitations, rights, and AI-skill links. Changes to underlying corpus data require corresponding corpus documentation, individual AI-skill, and master AI-skill updates and validation.

## Research landing page rollout (2026-10-15)

All 14 entries in `_data/corpora.yml` now have introductory landing pages linked from `/corpora/`. Repository existence was checked using the GitHub connector. These pages are discovery summaries, not certified corpus coverage reports. Public GitHub Pages deployment and generated sitemap have not yet been independently verified. Next: validate live build, confirm sitemap XML, configure Search Console, expand source-backed scholarship, and verify AI-skill links against each repository. No corpus records or AI skills were modified in this rollout.

## Automated portal validation

GitHub Actions workflow `validate-portal.yml` checks the 14 landing-page slugs, required research cautions, Jekyll build, generated sitemap URLs, and canonical tags. Review the workflow result under **Actions → Validate research portal**; a committed workflow is not evidence of a successful run. The workflow does not validate underlying inscription records or independent scholarly accuracy.

## Live deployment and Google Search Console checklist

1. In **Settings → Pages**, confirm the deployment source and successful publication at `https://hawkinsnick.github.io/Corpus-updates/`.
2. Open `https://hawkinsnick.github.io/Corpus-updates/sitemap.xml` and `https://hawkinsnick.github.io/Corpus-updates/linear-a/` and confirm the expected content is served.
3. In Google Search Console, add the **URL-prefix** property `https://hawkinsnick.github.io/Corpus-updates/` and complete the required ownership verification. GitHub Pages does not require a purchased domain.
4. Submit `https://hawkinsnick.github.io/Corpus-updates/sitemap.xml` in Search Console, inspect selected page URLs, and monitor indexing reports. Sitemap submission and indexing are not guarantees of ranking.
5. Audit landing pages for scholarly substance and verify any AI-skill links before promoting them to researchers.

Live Pages deployment and Google Search Console ownership require independent confirmation; they are not claimed complete by this repository update.
