package apcsa.TESTING;

import net.fabricmc.api.ModInitializer;

import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.fabricmc.fabric.api.object.builder.v1.block.FabricBlockSettings;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class APCSA_RENAME_ME implements ModInitializer {
	public static final String MOD_ID = "apcsa_rename_me";

	// This logger is used to write text to the console and the log file.
	// It is considered best practice to use your mod id as the logger's name.
	// That way, it's clear which mod wrote info, warnings, and errors.
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    // Default Block/Item settings
    // Unless these are good, you should make your own settings
    static final FabricItemSettings ITEM_DEFAULT_SETTINGS   = new FabricItemSettings();
    static final FabricBlockSettings BLOCK_DEFAULT_SETTINGS = FabricBlockSettings.create();

	@Override
	public void onInitialize() {
		// This code runs as soon as Minecraft is in a mod-load-ready state.
		// However, some things (like resources) may still be uninitialized.
		// Proceed with mild caution.

		ModBlocks.register();
		LOGGER.info("Hello Fabric world!");
	}
}
