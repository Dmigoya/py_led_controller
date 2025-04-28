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

    def is_meet_active(self):
        """
        Checks if there's a Google Meet tab open in Safari
        :return: True if Meet is active, False otherwise
        """
        urls = self.get_urls()
        return any("meet.google.com" in url.lower() for url in urls)

def main():
    safari = SafariController()
    
    if safari.is_safari_running():
        logging.info("Checking for Meet URLs...")
        if safari.is_meet_active():
            logging.info("Google Meet is active")
        else:
            logging.info("No Google Meet tabs found")
    else:
        logging.info("Safari is not running")

if __name__ == "__main__":
    main() 