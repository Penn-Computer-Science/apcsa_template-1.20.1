package apcsa.TESTING;

import net.fabricmc.api.ModInitializer;

public class ExampleModItems implements ModInitializer {
    @Override
    public void onInitialize() {
        ModItems.initialize();
    }
}