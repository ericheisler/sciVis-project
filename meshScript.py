#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def make_mesh_image(inFile, outFile):
    # create a new 'XML Partitioned Unstructured Grid Reader'
    bssn_gr_50000pvtu = XMLPartitionedUnstructuredGridReader(FileName=[inFile])
    bssn_gr_50000pvtu.CellArrayStatus = ['mpi_rank', 'cell_level']
    bssn_gr_50000pvtu.PointArrayStatus = ['U_ALPHA', 'U_CHI', 'U_K', 'U_GT0', 'U_SYMGT0', 'U_SYMGT2', 'U_SYMGT3', 'U_SYMGT4', 'U_SYMGT5', 'U_SYMAT0', 'U_SYMAT1', 'U_SYMAT2', 'U_SYMAT3', 'U_SYMAT4', 'C_HAM', 'C_MOM0', 'C_MOM1', 'C_MOM2', 'C_PSI4_REAL', 'C_PSI4_IMG']

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1095, 766]

    # set background color to white
    renderView1.Background = [1, 1, 1]
    # get color transfer function/color map for 'cell_level'
    cell_levelLUT = GetColorTransferFunction('cell_level')

    # get color legend/bar for cell_levelLUT in view renderView3
    cell_levelLUTColorBar = GetScalarBar(cell_levelLUT, renderView1)

    # Properties modified on cell_levelLUTColorBar
    cell_levelLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    cell_levelLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

    # show data in view
    bssn_gr_50000pvtuDisplay = Show(bssn_gr_50000pvtu, renderView1)
    # trace defaults for the display properties.
    bssn_gr_50000pvtuDisplay.Representation = 'Surface'
    bssn_gr_50000pvtuDisplay.ColorArrayName = [None, '']
    bssn_gr_50000pvtuDisplay.OSPRayScaleArray = 'C_HAM'
    bssn_gr_50000pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    bssn_gr_50000pvtuDisplay.SelectOrientationVectors = 'C_HAM'
    bssn_gr_50000pvtuDisplay.ScaleFactor = 80.0
    bssn_gr_50000pvtuDisplay.SelectScaleArray = 'C_HAM'
    bssn_gr_50000pvtuDisplay.GlyphType = 'Arrow'
    bssn_gr_50000pvtuDisplay.GlyphTableIndexArray = 'C_HAM'
    bssn_gr_50000pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
    bssn_gr_50000pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
    bssn_gr_50000pvtuDisplay.ScalarOpacityUnitDistance = 7.149796694772021
    bssn_gr_50000pvtuDisplay.GaussianRadius = 40.0
    bssn_gr_50000pvtuDisplay.SetScaleArray = ['POINTS', 'C_HAM']
    bssn_gr_50000pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    bssn_gr_50000pvtuDisplay.OpacityArray = ['POINTS', 'C_HAM']
    bssn_gr_50000pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'

    # reset view to fit data
    renderView1.ResetCamera()

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Slice'
    slice1 = Slice(Input=bssn_gr_50000pvtu)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # show data in view
    slice1Display = Show(slice1, renderView1)
    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = [None, '']
    slice1Display.OSPRayScaleArray = 'C_HAM'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'C_HAM'
    slice1Display.ScaleFactor = 80.0
    slice1Display.SelectScaleArray = 'C_HAM'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'C_HAM'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.GaussianRadius = 40.0
    slice1Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'C_HAM']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(bssn_gr_50000pvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(bssn_gr_50000pvtu)

    # create a new 'Slice'
    slice2 = Slice(Input=bssn_gr_50000pvtu)
    slice2.SliceType = 'Plane'
    slice2.SliceOffsetValues = [0.0]

    # Properties modified on slice2.SliceType
    slice2.SliceType.Normal = [0.0, 1.0, 0.0]

    # Properties modified on slice2.SliceType
    slice2.SliceType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    slice2Display = Show(slice2, renderView1)
    # trace defaults for the display properties.
    slice2Display.Representation = 'Surface'
    slice2Display.ColorArrayName = [None, '']
    slice2Display.OSPRayScaleArray = 'C_HAM'
    slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice2Display.SelectOrientationVectors = 'C_HAM'
    slice2Display.ScaleFactor = 80.0
    slice2Display.SelectScaleArray = 'C_HAM'
    slice2Display.GlyphType = 'Arrow'
    slice2Display.GlyphTableIndexArray = 'C_HAM'
    slice2Display.DataAxesGrid = 'GridAxesRepresentation'
    slice2Display.PolarAxes = 'PolarAxesRepresentation'
    slice2Display.GaussianRadius = 40.0
    slice2Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice2Display.OpacityArray = ['POINTS', 'C_HAM']
    slice2Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(bssn_gr_50000pvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(bssn_gr_50000pvtu)

    # create a new 'Slice'
    slice3 = Slice(Input=bssn_gr_50000pvtu)
    slice3.SliceType = 'Plane'
    slice3.SliceOffsetValues = [0.0]

    # Properties modified on slice3.SliceType
    slice3.SliceType.Normal = [0.0, 0.0, 1.0]

    # Properties modified on slice3.SliceType
    slice3.SliceType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    slice3Display = Show(slice3, renderView1)
    # trace defaults for the display properties.
    slice3Display.Representation = 'Surface'
    slice3Display.ColorArrayName = [None, '']
    slice3Display.OSPRayScaleArray = 'C_HAM'
    slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice3Display.SelectOrientationVectors = 'C_HAM'
    slice3Display.ScaleFactor = 80.0
    slice3Display.SelectScaleArray = 'C_HAM'
    slice3Display.GlyphType = 'Arrow'
    slice3Display.GlyphTableIndexArray = 'C_HAM'
    slice3Display.DataAxesGrid = 'GridAxesRepresentation'
    slice3Display.PolarAxes = 'PolarAxesRepresentation'
    slice3Display.GaussianRadius = 40.0
    slice3Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice3Display.OpacityArray = ['POINTS', 'C_HAM']
    slice3Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(bssn_gr_50000pvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice3.SliceType)

    # set active source
    SetActiveSource(slice1)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType)

    # set active source
    SetActiveSource(slice2)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice2.SliceType)

    # set active source
    SetActiveSource(slice1)

    # set scalar coloring
    ColorBy(slice1Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, False)

    # get color transfer function/color map for 'cell_level'
    cell_levelLUT = GetColorTransferFunction('cell_level')

    # change representation type
    slice1Display.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice2)

    # set scalar coloring
    ColorBy(slice2Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice2Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice2Display.SetScalarBarVisibility(renderView1, False)

    # change representation type
    slice2Display.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice3)

    # set scalar coloring
    ColorBy(slice3Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice3Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice3Display.SetScalarBarVisibility(renderView1, False)

    # change representation type
    slice3Display.SetRepresentationType('Points')

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    cell_levelLUT.ApplyPreset('jet', True)

    #### saving camera placements for all active views

    # current camera placement for renderView1
    #renderView1.CameraPosition = [-1284.2885666127127, -1177.029340643195, 554.9603223891501]
    #renderView1.CameraViewUp = [0.22334614879207598, 0.20554840620866996, 0.9528202089191977]
    #renderView1.CameraParallelScale = 692.8203230275509

    # get layout
    layout1 = GetLayout()

    # split cell
    layout1.SplitHorizontal(0, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'Render View'
    renderView2 = CreateView('RenderView')
    renderView2.ViewSize = [576, 693]
    renderView2.AnnotationColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid = 'GridAxes3DActor'
    renderView2.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
    renderView2.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
    renderView2.StereoType = 0
    renderView2.Background = [1.0, 1.0, 1.0]

    # init the 'GridAxes3DActor' selected for 'AxesGrid'
    renderView2.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.GridColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    renderView2.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # get color transfer function/color map for 'cell_level'
    cell_levelLUT = GetColorTransferFunction('cell_level')

    # get color legend/bar for cell_levelLUT in view renderView3
    cell_levelLUTColorBar = GetScalarBar(cell_levelLUT, renderView2)

    # Properties modified on cell_levelLUTColorBar
    cell_levelLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    cell_levelLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

    # place view in the layout
    layout1.AssignView(2, renderView2)

    # split cell
    layout1.SplitVertical(2, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'Render View'
    renderView3 = CreateView('RenderView')
    renderView3.ViewSize = [576, 331]
    renderView3.AnnotationColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid = 'GridAxes3DActor'
    renderView3.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
    renderView3.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
    renderView3.StereoType = 0
    renderView3.Background = [1.0, 1.0, 1.0]

    # init the 'GridAxes3DActor' selected for 'AxesGrid'
    renderView3.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.GridColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    renderView3.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # get color transfer function/color map for 'cell_level'
    cell_levelLUT = GetColorTransferFunction('cell_level')

    # get color legend/bar for cell_levelLUT in view renderView3
    cell_levelLUTColorBar = GetScalarBar(cell_levelLUT, renderView3)

    # Properties modified on cell_levelLUTColorBar
    cell_levelLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    cell_levelLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

    # place view in the layout
    layout1.AssignView(6, renderView3)

    # set active view
    SetActiveView(renderView2)

    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # show data in view
    slice1Display = Show(slice1, renderView2)
    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.AmbientColor = [0.0, 0.0, 0.0]
    slice1Display.ColorArrayName = [None, '']
    slice1Display.OSPRayScaleArray = 'C_HAM'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'C_HAM'
    slice1Display.ScaleFactor = 80.0
    slice1Display.SelectScaleArray = 'C_HAM'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'C_HAM'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.GaussianRadius = 40.0
    slice1Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'C_HAM']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # reset view to fit data
    renderView2.ResetCamera()

    # find source
    slice2 = FindSource('Slice2')

    # set active source
    SetActiveSource(slice2)

    # show data in view
    slice2Display = Show(slice2, renderView2)
    # trace defaults for the display properties.
    slice2Display.Representation = 'Surface'
    slice2Display.AmbientColor = [0.0, 0.0, 0.0]
    slice2Display.ColorArrayName = [None, '']
    slice2Display.OSPRayScaleArray = 'C_HAM'
    slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice2Display.SelectOrientationVectors = 'C_HAM'
    slice2Display.ScaleFactor = 80.0
    slice2Display.SelectScaleArray = 'C_HAM'
    slice2Display.GlyphType = 'Arrow'
    slice2Display.GlyphTableIndexArray = 'C_HAM'
    slice2Display.DataAxesGrid = 'GridAxesRepresentation'
    slice2Display.PolarAxes = 'PolarAxesRepresentation'
    slice2Display.GaussianRadius = 40.0
    slice2Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice2Display.OpacityArray = ['POINTS', 'C_HAM']
    slice2Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # find source
    slice3 = FindSource('Slice3')

    # set active source
    SetActiveSource(slice3)

    # show data in view
    slice3Display = Show(slice3, renderView2)
    # trace defaults for the display properties.
    slice3Display.Representation = 'Surface'
    slice3Display.AmbientColor = [0.0, 0.0, 0.0]
    slice3Display.ColorArrayName = [None, '']
    slice3Display.OSPRayScaleArray = 'C_HAM'
    slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice3Display.SelectOrientationVectors = 'C_HAM'
    slice3Display.ScaleFactor = 80.0
    slice3Display.SelectScaleArray = 'C_HAM'
    slice3Display.GlyphType = 'Arrow'
    slice3Display.GlyphTableIndexArray = 'C_HAM'
    slice3Display.DataAxesGrid = 'GridAxesRepresentation'
    slice3Display.PolarAxes = 'PolarAxesRepresentation'
    slice3Display.GaussianRadius = 40.0
    slice3Display.SetScaleArray = ['POINTS', 'C_HAM']
    slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice3Display.OpacityArray = ['POINTS', 'C_HAM']
    slice3Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # set scalar coloring
    ColorBy(slice3Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice3Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice3Display.SetScalarBarVisibility(renderView2, False)

    # get color transfer function/color map for 'cell_level'
    cell_levelLUT = GetColorTransferFunction('cell_level')

    # change representation type
    slice3Display.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice2)

    # set scalar coloring
    ColorBy(slice2Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice2Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice2Display.SetScalarBarVisibility(renderView2, False)

    # set active source
    SetActiveSource(slice1)

    # set scalar coloring
    ColorBy(slice1Display, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView2, False)

    # change representation type
    slice1Display.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice2)

    # change representation type
    slice2Display.SetRepresentationType('Points')

    # set active view
    SetActiveView(renderView3)

    # set active source
    SetActiveSource(slice1)

    # show data in view
    slice1Display_1 = Show(slice1, renderView3)
    # trace defaults for the display properties.
    slice1Display_1.Representation = 'Surface'
    slice1Display_1.AmbientColor = [0.0, 0.0, 0.0]
    slice1Display_1.ColorArrayName = [None, '']
    slice1Display_1.OSPRayScaleArray = 'C_HAM'
    slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display_1.SelectOrientationVectors = 'C_HAM'
    slice1Display_1.ScaleFactor = 80.0
    slice1Display_1.SelectScaleArray = 'C_HAM'
    slice1Display_1.GlyphType = 'Arrow'
    slice1Display_1.GlyphTableIndexArray = 'C_HAM'
    slice1Display_1.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display_1.PolarAxes = 'PolarAxesRepresentation'
    slice1Display_1.GaussianRadius = 40.0
    slice1Display_1.SetScaleArray = ['POINTS', 'C_HAM']
    slice1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display_1.OpacityArray = ['POINTS', 'C_HAM']
    slice1Display_1.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice1Display_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice1Display_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice1Display_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice1Display_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice1Display_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice1Display_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # reset view to fit data
    renderView3.ResetCamera()

    # set active source
    SetActiveSource(slice2)

    # show data in view
    slice2Display_1 = Show(slice2, renderView3)
    # trace defaults for the display properties.
    slice2Display_1.Representation = 'Surface'
    slice2Display_1.AmbientColor = [0.0, 0.0, 0.0]
    slice2Display_1.ColorArrayName = [None, '']
    slice2Display_1.OSPRayScaleArray = 'C_HAM'
    slice2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
    slice2Display_1.SelectOrientationVectors = 'C_HAM'
    slice2Display_1.ScaleFactor = 80.0
    slice2Display_1.SelectScaleArray = 'C_HAM'
    slice2Display_1.GlyphType = 'Arrow'
    slice2Display_1.GlyphTableIndexArray = 'C_HAM'
    slice2Display_1.DataAxesGrid = 'GridAxesRepresentation'
    slice2Display_1.PolarAxes = 'PolarAxesRepresentation'
    slice2Display_1.GaussianRadius = 40.0
    slice2Display_1.SetScaleArray = ['POINTS', 'C_HAM']
    slice2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
    slice2Display_1.OpacityArray = ['POINTS', 'C_HAM']
    slice2Display_1.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice2Display_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice2Display_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice2Display_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice2Display_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice2Display_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice2Display_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # set active source
    SetActiveSource(slice3)

    # show data in view
    slice3Display_1 = Show(slice3, renderView3)
    # trace defaults for the display properties.
    slice3Display_1.Representation = 'Surface'
    slice3Display_1.AmbientColor = [0.0, 0.0, 0.0]
    slice3Display_1.ColorArrayName = [None, '']
    slice3Display_1.OSPRayScaleArray = 'C_HAM'
    slice3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
    slice3Display_1.SelectOrientationVectors = 'C_HAM'
    slice3Display_1.ScaleFactor = 80.0
    slice3Display_1.SelectScaleArray = 'C_HAM'
    slice3Display_1.GlyphType = 'Arrow'
    slice3Display_1.GlyphTableIndexArray = 'C_HAM'
    slice3Display_1.DataAxesGrid = 'GridAxesRepresentation'
    slice3Display_1.PolarAxes = 'PolarAxesRepresentation'
    slice3Display_1.GaussianRadius = 40.0
    slice3Display_1.SetScaleArray = ['POINTS', 'C_HAM']
    slice3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
    slice3Display_1.OpacityArray = ['POINTS', 'C_HAM']
    slice3Display_1.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice3Display_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
    slice3Display_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice3Display_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
    slice3Display_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
    slice3Display_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
    slice3Display_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

    # set scalar coloring
    ColorBy(slice3Display_1, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice3Display_1.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice3Display_1.SetScalarBarVisibility(renderView3, False)

    # change representation type
    slice3Display_1.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice2)

    # set scalar coloring
    ColorBy(slice2Display_1, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice2Display_1.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice2Display_1.SetScalarBarVisibility(renderView3, False)

    # set active source
    SetActiveSource(slice1)

    # set scalar coloring
    ColorBy(slice1Display_1, ('CELLS', 'cell_level'))

    # rescale color and/or opacity maps used to include current data range
    slice1Display_1.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice1Display_1.SetScalarBarVisibility(renderView3, False)

    # change representation type
    slice1Display_1.SetRepresentationType('Points')

    # set active source
    SetActiveSource(slice2)

    # change representation type
    slice2Display_1.SetRepresentationType('Points')

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1284.2885666127127, -1177.029340643195, 554.9603223891501]
    renderView1.CameraViewUp = [0.22334614879207598, 0.20554840620866996, 0.9528202089191977]
    renderView1.CameraParallelScale = 692.8203230275509

    # current camera placement for renderView3
    renderView3.CameraPosition = [-5.906983245968588, -5.606502290368703, 3.0191783997690376]
    renderView3.CameraViewUp = [0.24263555726153785, 0.24924527861335263, 0.9375525464961072]
    renderView3.CameraParallelScale = 565.685424949238

    # current camera placement for renderView2
    renderView2.CameraPosition = [-87.29087225170377, -81.3945697281313, 38.00353920758871]
    renderView2.CameraViewUp = [0.2041670037060923, 0.22578934251017274, 0.9525413415734251]
    renderView2.CameraParallelScale = 565.685424949238

    #### uncomment the following to render all views
    RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).

    layout1 = GetLayout()
    SaveScreenshot(outFile, layout1, SaveAllViews=1, ImageResolution=[1166, 720])
    
    Disconnect()
    Connect()

#filenameNumbers = [0, 50000, 80000]
framenumbers = [90000 + i*1000 for i in range(107)]
filenameNumbers = []
for n in framenumbers:
	filenameNumbers.append(n)

for fnum in filenameNumbers:
    infile = '/scratch/kingspeak/serial/u1011531/GR/q1_d15_R1.00_wtol_1e-4/vtu/bssn_gr_'+str(fnum)+'.pvtu'
    outfile = 'meshvis_'+str(fnum)+'.png'
    
    print('preparing to make '+str(fnum))
    make_mesh_image(infile, outfile)
    print('finished '+str(fnum))
