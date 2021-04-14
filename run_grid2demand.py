import grid2demand as gd

"Step 1: Read Input Network Data"
gd.ReadNetworkFiles()

"Step 2: Partition Grid into cells"
gd.PartitionGrid(number_of_x_blocks=None, number_of_y_blocks=None, cell_width=500, cell_height=500)
# users can customize number of grid cells or cell's width and height in meters

"Step 3: Get Production/Attraction Rates of Each Land Use Type with a Specific Trip Purpose"
gd.GetPoiTripRate(trip_purpose=1)
# users can customize trip purpose and poi_trip_rate.csv

"Step 4: Define Production/Attraction Value of Each Node According to POI Type"
gd.GetNodeDemand(residential_production=20, residential_attraction=20, boundary_production=0, boundary_attraction=0)
# users can customize production and attraction values of residential nodes and boundary nodes

"Step 5: Calculate Zone-to-zone Accessibility Matrix by Centroid-to-centroid Straight Distance"
gd.ProduceAccessMatrix()

"Step 6: Apply Gravity Model to Perform Trip Distribution"
gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)
# users can customize friction factor coefficients under a specific trip purpose

"Step 7: Generate Agent"
gd.GenerateAgentBasedDemand()


