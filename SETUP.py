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

def renameFolder(path: str, name: str):
    folder = Path(path)

    new_path = folder.with_name(name)
    folder.rename(new_path)

    print(f"\tRenamed {path} to {new_path}")

def renameFile(path: str, name: str):
    file = Path(path)

    new_path = file.with_name(name)
    file.rename(new_path)

    print(f"\tRenamed {path} to {new_path}")

def replaceInFile(path:str, original:str, replace:str):
	filePath = Path(path)
	
	content = filePath.read_text()
	content = content.replace(original, replace)

	filePath.write_text(content)

	print(f"\tReplaced {original} with {replace} in file {path}")

def refactor(username:str, modname:str):
	print("Refactoring Template...")

	print("Renaming Files & Folders...")

	# Main
	renameFolder("src/main/java/apcsa/template", username)
	renameFolder("src/main/resources/assets/apcsa.template", username)
	renameFolder("src/main/resources/data/apcsa_rename_me", username)
	renameFile("src/main/resources/apcsa_rename_me.mixins.json", f"{username}.mixins.json")
	# Client
	renameFolder("src/client/java/apcsa/template", username)
	renameFile("src/client/resources/apcsa_rename_me.client.mixins.json", f"{username}.client.mixins.json")

	print("Replacing identifiers in files...")

	# Main
	replaceInFile(f"src/main/resources/assets/{username}/lang/en_us.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/{username}.mixins.json", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/resources/data/{username}/loot_tables/blocks/condensed_dirt.json", "apcsa_rename_me", username)
		# Tags
	replaceInFile(f"src/main/resources/data/minecraft/tags/blocks/mineable/shovel.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/data/minecraft/tags/blocks/needs_stone_tool.json", "apcsa_rename_me", username)
		# Block/Item Stuff
	replaceInFile(f"src/main/resources/assets/{username}/blockstates/condensed_dirt.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/block/condensed_dirt.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/item/condensed_dirt.json", "apcsa_rename_me", username)
	replaceInFile(f"src/main/resources/assets/{username}/models/item/test_item.json", "apcsa_rename_me", username)


	replaceInFile(f"src/main/resources/fabric.mod.json", "modid", username)
	replaceInFile(f"src/main/resources/fabric.mod.json", "ModName", modname)

	# Client
	replaceInFile(f"src/client/resources/{username}.client.mixins.json", "apcsa.template.client.mixin", f"apcsa.{username}.client.mixin")

	# -- INSIDE of the java files (pain) -- #
	# Main
	replaceInFile(f"src/main/java/apcsa/{username}/mixin/ExampleMixin.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/Mod.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/ModBlocks.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/main/java/apcsa/{username}/ModItems.java", "apcsa.template", f"apcsa.{username}")

	# Client
	replaceInFile(f"src/client/java/apcsa/{username}/client/mixin/ExampleClientMixin.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/client/java/apcsa/{username}/client/ModClient.java", "apcsa.template", f"apcsa.{username}")
	replaceInFile(f"src/client/java/apcsa/{username}/client/ModDataGenerator.java", "apcsa.template", f"apcsa.{username}")

	print("Refactoring finished!")

def MAIN():
	print("APCSA Fabric [1.20.1] Modding Template")

	print("Setting up Project...")

	# Since we have getpass we can guess what the username
	username = getpass.getuser()
	correct = checkBool(f"Is your username {getpass.getuser()} (Y/N)? ")
	if not correct:
		username = input("Input your username: ")
	
	modname = input("What is your mod's name? ")

	refactor(username, modname)
	input("Press enter to close.")


if __name__ == "__main__":
	MAIN()