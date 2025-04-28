import subprocess
import logging

class SafariController:
    def __init__(self):
        pass

    def is_safari_running(self):
        """
        Checks if Safari is running
        :return: True if Safari is running, False otherwise
        """
        script = '''
        tell application "System Events"
            return (exists process "Safari")
        end tell
        '''
        try:
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            return result.stdout.strip() == 'true'
        except Exception:
            return False

    def get_tabs(self):
        """
        Gets the list of open tabs in Safari
        :return: List of tab titles, empty list if Safari is not running
        """
        if not self.is_safari_running():
            logging.info("Safari is not running")
            return []

        script = '''
        tell application "Safari"
            set tabList to {}
            repeat with w in windows
                repeat with t in tabs of w
                    set end of tabList to name of t
                end repeat
            end repeat
            return tabList
        end tell
        '''
        try:
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            if result.returncode == 0:
                tabs = [tab.strip() for tab in result.stdout.split(',')]
                return tabs
            return []
        except Exception as e:
            logging.error(f"Error getting Safari tabs: {str(e)}")
            return []

    def get_urls(self):
        """
        Gets the list of URLs from open tabs in Safari
        :return: List of URLs, empty list if Safari is not running
        """
        if not self.is_safari_running():
            logging.info("Safari is not running")
            return []

        script = '''
        tell application "Safari"
            set urlList to {}
            repeat with w in windows
                repeat with t in tabs of w
                    set end of urlList to URL of t
                end repeat
            end repeat
            return urlList
        end tell
        '''
        try:
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            if result.returncode == 0:
                urls = [url.strip() for url in result.stdout.split(',')]
                return urls
            return []
        except Exception as e:
            logging.error(f"Error getting Safari URLs: {str(e)}")
            return []

def main():
    safari = SafariController()
    
    if safari.is_safari_running():
        logging.info("Open Safari tabs:")
        tabs = safari.get_tabs()
        for tab in tabs:
            logging.info(f"- {tab}")
        
        logging.info("\nSafari URLs:")
        urls = safari.get_urls()
        for url in urls:
            logging.info(f"- {url}")
    else:
        logging.info("Safari is not running")

if __name__ == "__main__":
    main() 