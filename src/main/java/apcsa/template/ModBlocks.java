package apcsa.template;

import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.fabricmc.fabric.api.object.builder.v1.block.FabricBlockSettings;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;

import java.util.ArrayList;
import java.util.List;

public class ModBlocks
{
    /** The list of blocks */
    public static final List<Block> MOD_BLOCKS = new ArrayList<>();

    /**
     * Makes a Block with settings
     *
     * @param blockSettings The settings for the block
     * @return The Block
     */
    static Block makeBlock(FabricBlockSettings blockSettings)
    {
        return new Block(blockSettings);
    }

    /**
     * Registers both the Block Item and the Block
     *
     * @param id The ID of the block (Ie: modid:myblock)
     * @param block The block that you're registering
     * @param itemSetting The item settings for when it's in the inventory
     */
    static void registerBlock(String id, Block block, FabricItemSettings itemSetting)
    {
        // The block item for the block (So it shows up in the inventory)
        final Item _ITEM = new BlockItem(block, itemSetting);

        // Adds the block to the ArrayList so you can access it *before* it's registered
        //      Ie: A class that accesses Blocks that runs before registration
        MOD_BLOCKS.add(block);

        // Add the block to the register
        Registry.register(BuiltInRegistries.BLOCK, new ResourceLocation(Mod.MOD_ID, id), block);
        // Add the block item to the register
        Registry.register(BuiltInRegistries.ITEM, new ResourceLocation(Mod.MOD_ID, id), _ITEM);
    }

    // Blocks
    public static final Block TEST_BLOCK = makeBlock(
            FabricBlockSettings.create()
                .requiresTool()
                .strength(3.0f, 3.0f));

    /**
     * Registers all the blocks
     */
    public static void register()
    {
        // Put your blocks here
        registerBlock("test_block", TEST_BLOCK, Mod.ITEM_DEFAULT_SETTINGS);
    }
}
