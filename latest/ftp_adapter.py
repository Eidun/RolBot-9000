import ftplib


class FTPFile:

    def __init__(self, name, modify, path='/'):
        self.name = name
        self.modify = modify
        self.date = int(self.parse_date())
        if path is not '/':
            path += '/'
        self.path = path

    def parse_date(self):
        number_date = self.modify.split('=')
        return number_date[1]


# Numeric position of the required data in the array
NAME_POSITION = 7
DATE_POSITION = 2
# Server host and credentials. You can export to other files, or env variables.
HOST = 'ams22.stablehost.com'
HTTP_HOST = 'http://dd.atelierdunoir.org'
USER = 'eidun@dd.atelierdunoir.org'
PASS = 'password123'
# Supported formats, you can add more to this list
ALLOWED_FORMATS = ['zip', 'rar']
FORBIDDEN_FOLDERS = ['application']


def connect():
    # Connects to the FTP server
    ftp = ftplib.FTP(HOST)
    ftp.login(user=USER, passwd=PASS)
    return ftp


def get_last_file_url(subdir: str):
    try:
        # Get connection
        ftp = connect()

        # Get all files
        files = get_subdir_files_rec(subdir, ftp)

        # Sort list by date
        files = sorted(files, key=lambda x: x.date, reverse=True)
        # Return the latest file
        if len(files) > 0:
            return files[0]
        return FTPFile('No file found there!', 'modify=0')
    except ftplib.error_perm:
        print('No such directory')
        return FTPFile(' Directory not found', 'modify=0')
    except ftplib.error_proto:
        print('Error connection to the FTP server')
        return None


def get_subdir_files_rec(subdir, ftp):

    # Navigate to subdir
    if subdir is not None:
        ftp.cwd(subdir)
    # Get all data
    raw_data = []
    # Data separated with semi-colons
    ftp.retrlines('MLSD', raw_data.append)
    # Get files from raw_data
    files = files_from_raw_data(raw_data, ftp)
    # Go father dir
    if subdir is not None:
        ftp.cwd('..')
    return files


def files_from_raw_data(raw_data, ftp):
    files_list = []
    for line in raw_data:
        # Separate values
        values = line.split(';')
        name = values[NAME_POSITION]
        # Remove whitespace
        name = name[1:]
        date = values[DATE_POSITION]
        if name.startswith('.'):  # Metadata files not added
            continue
        name_split = name.split('.')
        length = len(name_split)
        if length < 2:  # It's s subdir, not a file
            if name_split[0] in FORBIDDEN_FOLDERS:
                continue
            subdir_files = get_subdir_files_rec(name_split[0], ftp)
            files_list.extend(subdir_files)
        if name_split[length - 1] not in ALLOWED_FORMATS:  # Unwanted format
            continue
        # Create object file with name and date
        file = FTPFile(name, date, ftp.pwd())
        files_list.append(file)
    return files_list





