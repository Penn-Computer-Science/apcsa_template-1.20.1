package apcsa.TESTING;


import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;

public class ModItems
{
    static Item makeItem(FabricItemSettings itemSettings)
    {
        return new Item(itemSettings);
    }

    public static final Item TEST_ITEM = makeItem(APCSA_RENAME_ME.ITEM_DEFAULT_SETTINGS);

    public static void register()
    {
        Registry.register(BuiltInRegistries.ITEM, new ResourceLocation(APCSA_RENAME_ME.MOD_ID, "test_item"), TEST_ITEM);
    }
}