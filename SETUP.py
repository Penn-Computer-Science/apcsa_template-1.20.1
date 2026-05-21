import getpass
import os
import sys

from pathlib import Path

# Colors 'n Stuff
def supports_color():
	# Not a terminal
	if not sys.stdout.isatty():
		return False

	# Windows
	if os.name == "nt":
		try:
			import ctypes

			kernel32 = ctypes.windll.kernel32

			# Enable VT processing on Windows console
			handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE

			mode = ctypes.c_uint32()

			if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
				ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

				kernel32.SetConsoleMode(
					handle,
					mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
				)

				return True

		except:
			return False

		return False

	# Unix/Linux/macOS
	term = os.environ.get("TERM", "")
	return term != "" and term != "dumb"

USE_COLOR = supports_color()

def color(text, code):
    if USE_COLOR:
        return f"\033[{code}m{text}\033[0m"
    return text

def prGreen(s):
    print(color(s, "1;92"))

def prCyan(s):
    print(color(s, "0;96"))

def prLightGray(s):
    print(color(s, "1;97"))

def prRed(s):
	print(color(s, "1;91"))

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

	if not folder.exists():
		prRed(f"\tFolder {path} does not exist")
		return

	new_path = folder.with_name(name)
	folder.rename(new_path)

	prCyan(f"\tRenamed {path} to {new_path}")

def renameFile(path:str, name:str):
	file = Path(path)

	if not file.exists():
		prRed(f"\tFile {path} does not exist")
		return

	new_path = file.with_name(name)
	file.rename(new_path)

	prCyan(f"\tRenamed {path} to {new_path}")

def replaceInFile(path:str, original:str, replace:str):
	filePath = Path(path)

	if not filePath.exists():
		prRed(f"\tFile {path} does not exist")
		return

	content = filePath.read_text()
	content = content.replace(original, replace)

	filePath.write_text(content)

	prCyan(f"\tReplaced {original} with {replace} in file {path}")

def refactor(username:str, modname:str):
	prLightGray("Refactoring Template...")

	prLightGray("Renaming Files & Folders...")

	# Main
	renameFolder("src/main/java/apcsa/template", username)
	renameFolder("src/main/resources/assets/apcsa.template", username)
	renameFolder("src/main/resources/data/apcsa_rename_me", username)
	renameFile("src/main/resources/apcsa_rename_me.mixins.json", f"{username}.mixins.json")
	# Client
	renameFolder("src/client/java/apcsa/template", username)
	renameFile("src/client/resources/apcsa_rename_me.client.mixins.json", f"{username}.client.mixins.json")

	prLightGray("\n[Main] Replacing identifiers in files...")

	# Main
	replaceInFile(f"src/main/resources/assets/{username}/lang/en_us.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/{username}.mixins.json", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/resources/data/{username}/loot_tables/blocks/test_block.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/data/{username}/recipes/test_block.json", "apcsa", username)

	# Tags
	prLightGray("\nReplacing tag indetifiers...")
	replaceInFile(f"src/main/resources/data/minecraft/tags/blocks/mineable/pickaxe.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/data/minecraft/tags/blocks/needs_stone_tool.json", "apcsa_rename_me", username)

	# Block/Item Stuff
	prLightGray("\nReplacing model/blockstate identifiers...")
	replaceInFile(f"src/main/resources/assets/{username}/blockstates/test_block.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/block/test_block.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/item/test_block.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/item/test_item.json", "apcsa_rename_me", username)

	prLightGray("\nReplacing identifiers in fabric mod...")
	replaceInFile(f"src/main/resources/fabric.mod.json", "modid", username)
	replaceInFile(f"src/main/resources/fabric.mod.json", "ModName", modname)

	# Client
	prLightGray("\n[Client] Replacing identifiers in files...")
	replaceInFile(f"src/client/resources/{username}.client.mixins.json", "apcsa.template.client.mixin", f"apcsa.{username}.client.mixin")

	# -- INSIDE of the java files (pain) -- #

	# Main
	prLightGray("\n[Main] Replacing identifiers in java classes...")
	replaceInFile(f"src/main/java/apcsa/{username}/mixin/ExampleMixin.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/Mod.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/Mod.java", "modid", username)
	replaceInFile(f"src/main/java/apcsa/{username}/ModBlocks.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/ModItems.java", "apcsa.template", f"apcsa.{username}")

	# Client
	prLightGray("\n[Client] Replacing identifiers in java classes...")
	replaceInFile(f"src/client/java/apcsa/{username}/client/mixin/ExampleClientMixin.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/client/java/apcsa/{username}/client/ModClient.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/client/java/apcsa/{username}/client/ModDataGenerator.java", "apcsa.template", f"apcsa.{username}")

	# Gradle
	prLightGray("\nUpdating identifiers in gradle files...")
	replaceInFile("gradle.properties", "template", username)
	replaceInFile("build.gradle", "apcsa_rename_me", username)
	replaceInFile("settings.gradle", "apcsa_rename_me", username)

	prGreen("\nRefactoring finished!")

def MAIN():
	print("-- APCSA Fabric [1.20.1] Modding Template --")

	print("Setting up Project...\n")

	# Since we have getpass we can guess what the username
	username:str = getpass.getuser()
	correct:bool = checkBool(f"Is your username {getpass.getuser()} (Y/N)? ")
	if not correct:
		username = input("Input your username: ")
	
	modname:str = input("What is your mod's name? ")

	refactor(username.lower(), modname)
	input("\nPress enter to close.")


if __name__ == "__main__":
	MAIN()