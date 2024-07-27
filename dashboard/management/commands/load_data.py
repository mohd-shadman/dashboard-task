
import json
import io
from dateutil import parser
from dateutil.parser import ParserError
from django.core.management.base import BaseCommand
from dashboard.models import DataEntry
from django.utils import timezone
import pytz 
import pandas as pd


class Command(BaseCommand):
    help = 'Load data from json file into database'

    def handle(self, *args, **kwargs):
        def parse_date(date_str):
            if date_str:
                try:
                    # Parse the date string into a naive datetime object
                    naive_date = parser.parse(date_str)
                    # Convert naive datetime to a timezone-aware datetime
                    return timezone.make_aware(naive_date, pytz.utc)
                except (ParserError, ValueError):
                    self.stderr.write(f"Error parsing date: {date_str}")
            return timezone.now()

        def parse_int(value, default=0):
            try:
                return int(value)
            except (ValueError, TypeError):
                return default

        try:
            with io.open('jsondata.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                # Convert JSON to DataFrame for easier manipulation
                df = pd.DataFrame(data)

                # Clean the data
                df.fillna({
                    'title': 'Unknown',
                    'topic': 'Unknown',
                    'sector': 'Unknown',
                    'region': 'Unknown',
                    'intensity': 0,
                    'relevance': 0,
                    'likelihood': 0,
                    'source': 'Unknown',
                    'url': ''
                }, inplace=True)

                # Ensure numerical fields are valid integers
                df['intensity'] = df['intensity'].apply(lambda x: parse_int(x))
                df['relevance'] = df['relevance'].apply(lambda x: parse_int(x))
                df['likelihood'] = df['likelihood'].apply(lambda x: parse_int(x))

                df.drop_duplicates(inplace=True)

                df['region'] = df['region'].str.title()

                df = df[df['title'] != '']

                # Count of successfully created entries
                count = 0
                for entry in df.to_dict(orient='records'):
                    try:
                        DataEntry.objects.create(
                            end_year=entry.get('end_year', ''),
                            intensity=entry.get('intensity', 0),
                            sector=entry.get('sector', ''),
                            topic=entry.get('topic', ''),
                            insight=entry.get('insight', ''),
                            url=entry.get('url', ''),
                            region=entry.get('region', ''),
                            start_year=entry.get('start_year', ''),
                            impact=entry.get('impact', ''),
                            added=parse_date(entry.get('added')),
                            published=parse_date(entry.get('published')),
                            country=entry.get('country', ''),
                            relevance=entry.get('relevance', 0),
                            pestle=entry.get('pestle', ''),
                            source=entry.get('source', ''),
                            title=entry.get('title', ''),
                            likelihood=entry.get('likelihood', 0),
                        )
                        count += 1
                    except Exception as e:
                        self.stderr.write(f"Error creating entry: {e}")

                self.stdout.write(f"Data loaded successfully: {count} entries created.")
        except Exception as e:
            self.stderr.write(f"Error loading data: {e}")
