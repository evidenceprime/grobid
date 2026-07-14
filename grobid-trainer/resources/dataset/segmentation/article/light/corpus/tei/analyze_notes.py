#!/usr/bin/env python3
import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
import difflib

def extract_notes_from_file(file_path):
    """Extract headnote and footnote content from a TEI XML file"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Handle namespace
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        headnotes = []
        footnotes = []
        
        # Extract all note elements
        for note in root.findall('.//tei:note', ns):
            place = note.get('place', '')
            if place == 'headnote':
                # Get all text content, handling <lb/> tags
                text_parts = []
                for elem in note.iter():
                    if elem.text:
                        text_parts.append(elem.text)
                    if elem.tail:
                        text_parts.append(elem.tail)
                    if elem.tag == '{http://www.tei-c.org/ns/1.0}lb':
                        text_parts.append(' ')
                content = ''.join(text_parts).strip()
                if content:
                    headnotes.append(content)
            elif place == 'footnote':
                # Get all text content, handling <lb/> tags
                text_parts = []
                for elem in note.iter():
                    if elem.text:
                        text_parts.append(elem.text)
                    if elem.tail:
                        text_parts.append(elem.tail)
                    if elem.tag == '{http://www.tei-c.org/ns/1.0}lb':
                        text_parts.append(' ')
                content = ''.join(text_parts).strip()
                if content:
                    footnotes.append(content)
        
        return headnotes, footnotes
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return [], []

def normalize_text(text):
    """Normalize text for comparison by removing extra whitespace and standardizing"""
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text

def find_similar_content(list1, list2, threshold=0.8):
    """Find similar content between two lists using difflib similarity ratio"""
    matches = []
    for item1 in list1:
        norm1 = normalize_text(item1)
        for item2 in list2:
            norm2 = normalize_text(item2)
            # Only compare if both have substantial content (more than just common words)
            if len(norm1) > 10 and len(norm2) > 10:
                similarity = difflib.SequenceMatcher(None, norm1, norm2).ratio()
                if similarity >= threshold:
                    matches.append((item1, item2, similarity))
    return matches

def main():
    tei_dir = '.'
    inconsistent_files = []
    
    # Get all TEI XML files
    tei_files = [f for f in os.listdir(tei_dir) if f.endswith('.tei.xml')]
    
    for filename in tei_files:
        file_path = os.path.join(tei_dir, filename)
        headnotes, footnotes = extract_notes_from_file(file_path)
        
        if headnotes and footnotes:
            # Look for exact or near-exact matches
            exact_matches = []
            similar_matches = []
            
            # Check for exact matches (after normalization)
            headnote_norms = [normalize_text(h) for h in headnotes]
            footnote_norms = [normalize_text(f) for f in footnotes]
            
            for i, h_norm in enumerate(headnote_norms):
                for j, f_norm in enumerate(footnote_norms):
                    if h_norm == f_norm and len(h_norm) > 10:  # Only meaningful content
                        exact_matches.append((headnotes[i], footnotes[j]))
            
            # Check for similar content
            if not exact_matches:
                similar_matches = find_similar_content(headnotes, footnotes, threshold=0.85)
            
            if exact_matches or similar_matches:
                inconsistent_files.append({
                    'file': filename,
                    'exact_matches': exact_matches,
                    'similar_matches': similar_matches,
                    'all_headnotes': headnotes,
                    'all_footnotes': footnotes
                })
    
    # Report results
    print(f"Found {len(inconsistent_files)} files with inconsistencies out of {len(tei_files)} total files")
    print("=" * 80)
    
    for file_info in inconsistent_files:
        print(f"\nFILE: {file_info['file']}")
        print("-" * 60)
        
        if file_info['exact_matches']:
            print("EXACT MATCHES:")
            for h, f in file_info['exact_matches']:
                print(f"  Headnote: {h[:100]}...")
                print(f"  Footnote: {f[:100]}...")
                print()
        
        if file_info['similar_matches']:
            print("SIMILAR MATCHES:")
            for h, f, sim in file_info['similar_matches']:
                print(f"  Similarity: {sim:.2f}")
                print(f"  Headnote: {h[:100]}...")
                print(f"  Footnote: {f[:100]}...")
                print()

if __name__ == "__main__":
    main()
