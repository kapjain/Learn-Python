"""
Implement a group_by_owners function that:

    Accepts a dictionary containing the file owner name for each file name.
    Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

"""
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        rfiles = {}
        for key, value in files.items():
            if not value in rfiles.keys():
                rfiles[value] = []
            for key1, value1 in files.items():
                if not key1 in rfiles[value] and value1 == value:
                    rfiles[value].append(key1)
                      
        return rfiles

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))