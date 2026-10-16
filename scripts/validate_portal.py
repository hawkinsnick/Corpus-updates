#!/usr/bin/env python3
"""Dependency-free validation of research portal navigation and generated SEO files."""
import argparse
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED = ('linear-a','linear-b','cypro-minoan','cretan-hieroglyphs',
 'phaistos-disc','byblos-syllabary','cypriot-syllabic-greek',
 'eteocypriot','eteocretan','lycian-carian','phrygian',
 'anatolian-hieroglyphic','archanes-script','aegean-anomalous')


def validate_source():
    errors = []
    data = (ROOT / '_data/corpora.yml').read_text()
    slugs = re.findall(r'^  page: /([^/]+)/$', data, re.M)
    if sorted(slugs) != sorted(EXPECTED):
        errors.append('Corpus directory slugs differ from the 14 expected pages')
    for slug in EXPECTED:
        path = ROOT / slug / 'index.html'
        if not path.is_file():
            errors.append(f'Missing landing page: {path}')
            continue
        page = path.read_text()
        for required in ('layout: default', 'description:', '<h1>', '/issues/new', 'licens'):
            if required.lower() not in page.lower():
                errors.append(f'{slug}: missing required text: {required}')
    for path in ('index.html','corpora/index.html','updates/index.html',
                 'contribute/index.html','sitemap.xml','robots.txt'):
        if not (ROOT / path).is_file():
            errors.append(f'Missing required file: {path}')
    return errors


def validate_rendered(site):
    errors = []
    sitemap = site / 'sitemap.xml'
    if not sitemap.is_file():
        return ['Generated sitemap.xml missing']
    try:
        root = ET.parse(sitemap).getroot()
        locs = [node.text or '' for node in root.iter() if node.tag.endswith('}loc')]
        for slug in EXPECTED:
            if not any(f'/{slug}/' in url for url in locs):
                errors.append(f'Sitemap missing {slug}')
        if not all(u.startswith('https://hawkinsnick.github.io/Corpus-updates/') for u in locs):
            errors.append('Sitemap contains URLs outside expected GitHub Pages base')
    except ET.ParseError as exc:
        errors.append(f'Invalid sitemap XML: {exc}')
    for slug in EXPECTED:
        page = site / slug / 'index.html'
        if not page.is_file():
            errors.append(f'Jekyll did not generate {slug}')
        elif '<link rel="canonical"' not in page.read_text():
            errors.append(f'Missing canonical URL: {slug}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rendered', type=pathlib.Path)
    args = parser.parse_args()
    issues = validate_rendered(args.rendered) if args.rendered else validate_source()
    for issue in issues:
        print('ERROR:', issue)
    print('PASS' if not issues else f'FAIL: {len(issues)} issues')
    sys.exit(bool(issues))
