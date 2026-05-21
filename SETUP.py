import getpass
from pathlib import Path

def checkBool(prefix:str):
	while True:
		val = input(prefix)
		if val.lower() == "y":
			return True
		elif val.lower() == "n":
			return False
		
		print("Please put Y or N.")

def renameFolder(path:str, name:str):
	folder = Path(path)
	folder.rename(name)

	print(f"Renamed {path}'s name to {name}")

def replaceInFile(path:str, original:str, replace:str):
	filePath = Path(path)
	
	content = filePath.read_text()
	content = content.replace(original, replace)

	filePath.write_text(content)

	print(f"Replaced {original} with {replace} in file {path}")

def MAIN():
	print("APCSA Fabric [1.20.1] Modding Template")

	print("Setting up Project...")

	# Since we have getpass we can guess what the username
	username = getpass.getuser()
	correct = checkBool(f"Is your username {getpass.getuser()} (Y/N)? ")
	if not correct:
		username = input("Input your username: ")
	
	modname = input("What is your mod's name? ")

	print("Refactoring Template...")

	print("Renaming Folders...")
	renameFolder("src/main/java/apcsa/template", username)
	renameFolder("src/main/resources/apcsa.template", username)
	renameFolder("src/main/resources/apcsa.template", username)
	renameFolder("src/main/resources/apcsa_rename_me", username)
	renameFolder("src/client/java/apcsa/template", username)

	print("Refactoring finished!")
	input("Press enter to close.")


if __name__ == "__main__":
	MAIN()