from bs4 import BeautifulSoup
import requests
from Course import Course

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        """Fetch and return the parsed HTML document"""
        doc = BeautifulSoup(
            requests.get(
                "http://learn-co-curriculum.github.io/site-for-scraping/courses"
            ).text,
            'html.parser'
        )
        return doc

    def get_courses(self):
        """Return all course elements from the page"""
        return self.get_page().select('.post')

    def make_courses(self):
        """Create Course objects from scraped data"""
        for course in self.get_courses():
            # Extract title, schedule, and description with fallback to empty string
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''
            
            # Create new Course object and add to courses list
            new_course = Course(title, date, description)
            self.courses.append(new_course)
        
        return self.courses

    def print_courses(self):
        """Print all courses"""
        for course in self.make_courses():
            print(course)