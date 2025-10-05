public class ProgrammaticGuiTestFarmflow {
    public static void main(String[] args) throws Exception {
        final java.util.concurrent.atomic.AtomicReference<GeneratedFarmflow> ref = new java.util.concurrent.atomic.AtomicReference<>();

        javax.swing.SwingUtilities.invokeAndWait(() -> {
            GeneratedFarmflow g = new GeneratedFarmflow();
            g.setVisible(true);
            ref.set(g);
        });

        GeneratedFarmflow g = ref.get();
        if (g == null)
            throw new IllegalStateException("GUI not created");

        // Programmatically populate farmer fields and click Add Farmer
        g.setField("farmer_name", "Test Farmer");
        g.setField("farmer_phone", "03000000000");
        g.setField("farmer_village", "TestVillage");
        g.clickButton("Add Farmer");

        // Now add a bill
        g.setField("bill_date", "2025-09-14");
        g.setField("bill_farmer", "Test Farmer");
        g.setField("bill_crop", "Wheat");
        g.setField("bill_weight", "10");
        g.setField("bill_rate", "50");
        g.clickButton("Add Bill");

        // Read totals using public helper
        String totals = g.getFieldText("totals");
        System.out.println("TOTALS:" + totals);
        // Give UI a moment to update
        Thread.sleep(200);
        System.out.println("(Programmatic test finished — totals reflected above)");
    }
}
