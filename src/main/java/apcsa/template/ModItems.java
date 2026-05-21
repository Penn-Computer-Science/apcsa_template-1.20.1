package apcsa.template;


import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;

public class ModItems
{
	/**
	 * Makes an Item with settings
	 * 
	 * @param itemSettings The settings for the item
	 * @return The Item
	 */
    static Item makeItem(FabricItemSettings itemSettings)
    {
        return new Item(itemSettings);
    }

	/**
	 * Registers an Item
	 * 
	 * @param id The ID of the block (Ie: modid:myitem)
	 * @param item The Item to be registered
	 */
	static void registerItem(String id, Item item)
	{
		Registry.register(BuiltInRegistries.ITEM, new ResourceLocation(Mod.MOD_ID, id), item);
	}

	// Items
    public static final Item TEST_ITEM = makeItem(Mod.ITEM_DEFAULT_SETTINGS);

	/**
	 * Registers all the items
	 */
    public static void register()
    {
		// Put your items here
        registerItem("test_item", TEST_ITEM);
    }
}