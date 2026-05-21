package apcsa.TESTING;

import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;

public class ModBlocks {
	public static final Block CONDENSED_DIRT = registerBlock(
			"condensed_dirt",
			new Block(BlockBehaviour.Properties.of()
					.strength(1.0F, 1.0F)
					.sound(SoundType.GRAVEL)
					.requiresCorrectToolForDrops())
	);


	public static void initialize() {
		ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.NATURAL_BLOCKS).register(entries -> {
			entries.accept(CONDENSED_DIRT);
		});
	}

	private static Block registerBlock(String name, Block block) {
		registerBlockItem(name, block);
		return Registry.register(BuiltInRegistries.BLOCK, id(name), block);
	}

	private static void registerBlockItem(String name, Block block) {
		Registry.register(BuiltInRegistries.ITEM, id(name), new BlockItem(block, new Item.Properties()));
	}

	private static ResourceLocation id(String name) {
		return new ResourceLocation(APCSA_RENAME_ME.MOD_ID, name);
	}
}
