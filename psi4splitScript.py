#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def make_mesh_image(inFile, outFile):
    # create a new 'XML Partitioned Unstructured Grid Reader'
    bssn_gr_160000pvtu = XMLPartitionedUnstructuredGridReader(FileName=[inFile])
    bssn_gr_160000pvtu.CellArrayStatus = ['mpi_rank', 'cell_level']
    bssn_gr_160000pvtu.PointArrayStatus = ['U_ALPHA', 'U_CHI', 'U_K', 'U_GT0', 'U_SYMGT0', 'U_SYMGT2', 'U_SYMGT3', 'U_SYMGT4', 'U_SYMGT5', 'U_SYMAT0', 'U_SYMAT1', 'U_SYMAT2', 'U_SYMAT3', 'U_SYMAT4', 'C_HAM', 'C_MOM0', 'C_MOM1', 'C_MOM2', 'C_PSI4_REAL', 'C_PSI4_IMG']

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1083, 756]
    renderView1.ViewSize = [1600, 800]

    # show data in view
    bssn_gr_160000pvtuDisplay = Show(bssn_gr_160000pvtu, renderView1)
    # trace defaults for the display properties.
    bssn_gr_160000pvtuDisplay.Representation = 'Surface'
    bssn_gr_160000pvtuDisplay.ColorArrayName = [None, '']
    bssn_gr_160000pvtuDisplay.OSPRayScaleArray = 'C_HAM'
    bssn_gr_160000pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    bssn_gr_160000pvtuDisplay.SelectOrientationVectors = 'C_HAM'
    bssn_gr_160000pvtuDisplay.ScaleFactor = 80.0
    bssn_gr_160000pvtuDisplay.SelectScaleArray = 'C_HAM'
    bssn_gr_160000pvtuDisplay.GlyphType = 'Arrow'
    bssn_gr_160000pvtuDisplay.GlyphTableIndexArray = 'C_HAM'
    bssn_gr_160000pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
    bssn_gr_160000pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
    bssn_gr_160000pvtuDisplay.ScalarOpacityUnitDistance = 8.575468788995424
    bssn_gr_160000pvtuDisplay.GaussianRadius = 40.0
    bssn_gr_160000pvtuDisplay.SetScaleArray = ['POINTS', 'C_HAM']
    bssn_gr_160000pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    bssn_gr_160000pvtuDisplay.OpacityArray = ['POINTS', 'C_HAM']
    bssn_gr_160000pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'

    # reset view to fit data
    renderView1.ResetCamera()

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Clip'
    clip1 = Clip(Input=bssn_gr_160000pvtu)
    clip1.ClipType = 'Plane'
    clip1.Scalars = ['POINTS', 'C_HAM']
    clip1.Value = 2.2429097344483675
    
    # Properties modified on clip2.ClipType
    clip1.ClipType.Normal = [-1.0, 0.0, 0.0]

    # show data in view
    clip1Display = Show(clip1, renderView1)
    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = [None, '']
    clip1Display.OSPRayScaleArray = 'C_HAM'
    clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip1Display.SelectOrientationVectors = 'C_HAM'
    clip1Display.ScaleFactor = 80.0
    clip1Display.SelectScaleArray = 'C_HAM'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.GlyphTableIndexArray = 'C_HAM'
    clip1Display.DataAxesGrid = 'GridAxesRepresentation'
    clip1Display.PolarAxes = 'PolarAxesRepresentation'
    clip1Display.ScalarOpacityUnitDistance = 9.262946326678488
    clip1Display.GaussianRadius = 40.0
    clip1Display.SetScaleArray = ['POINTS', 'C_HAM']
    clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip1Display.OpacityArray = ['POINTS', 'C_HAM']
    clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(bssn_gr_160000pvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(clip1)

    # create a new 'Clip'
    clip2 = Clip(Input=clip1)
    clip2.ClipType = 'Plane'
    clip2.Scalars = ['POINTS', 'C_HAM']
    clip2.Value = 2.2429097344483675

    # init the 'Plane' selected for 'ClipType'
    clip2.ClipType.Origin = [200.0, 0.0, 0.0]

    # Properties modified on clip2.ClipType
    clip2.ClipType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    clip2Display = Show(clip2, renderView1)
    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'
    clip2Display.ColorArrayName = [None, '']
    clip2Display.OSPRayScaleArray = 'C_HAM'
    clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip2Display.SelectOrientationVectors = 'C_HAM'
    clip2Display.ScaleFactor = 80.0
    clip2Display.SelectScaleArray = 'C_HAM'
    clip2Display.GlyphType = 'Arrow'
    clip2Display.GlyphTableIndexArray = 'C_HAM'
    clip2Display.DataAxesGrid = 'GridAxesRepresentation'
    clip2Display.PolarAxes = 'PolarAxesRepresentation'
    clip2Display.ScalarOpacityUnitDistance = 9.522389441534603
    clip2Display.GaussianRadius = 40.0
    clip2Display.SetScaleArray = ['POINTS', 'C_HAM']
    clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip2Display.OpacityArray = ['POINTS', 'C_HAM']
    clip2Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(clip1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(bssn_gr_160000pvtu)

    # create a new 'Slice'
    slice1 = Slice(Input=bssn_gr_160000pvtu)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]

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
    Hide(bssn_gr_160000pvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(slice1Display, ('POINTS', 'C_PSI4_REAL'))

    # rescale color and/or opacity maps used to include current data range
    slice1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'C_PSI4_REAL'
    c_PSI4_REALLUT = GetColorTransferFunction('C_PSI4_REAL')

    # Rescale transfer function
    c_PSI4_REALLUT.RescaleTransferFunction(-2e-05, 2e-05)

    # get opacity transfer function/opacity map for 'C_PSI4_REAL'
    c_PSI4_REALPWF = GetOpacityTransferFunction('C_PSI4_REAL')

    # Rescale transfer function
    c_PSI4_REALPWF.RescaleTransferFunction(-2e-05, 2e-05)

    # set active source
    SetActiveSource(clip1)

    # create a new 'Contour'
    contour1 = Contour(Input=clip2)
    contour1.ContourBy = ['POINTS', 'C_PSI4_REAL']
    contour1.Isosurfaces = [-2e-06]
    contour1.PointMergeMethod = 'Uniform Binning'

    # show data in view
    contour1Display = Show(contour1, renderView1)
    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'
    contour1Display.ColorArrayName = [None, '']
    contour1Display.OSPRayScaleArray = 'C_HAM'
    contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour1Display.SelectOrientationVectors = 'C_HAM'
    contour1Display.ScaleFactor = 80.0
    contour1Display.SelectScaleArray = 'C_HAM'
    contour1Display.GlyphType = 'Arrow'
    contour1Display.GlyphTableIndexArray = 'C_HAM'
    contour1Display.DataAxesGrid = 'GridAxesRepresentation'
    contour1Display.PolarAxes = 'PolarAxesRepresentation'
    contour1Display.GaussianRadius = 40.0
    contour1Display.SetScaleArray = ['POINTS', 'C_HAM']
    contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour1Display.OpacityArray = ['POINTS', 'C_HAM']
    contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(clip1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(clip1)

    # show data in view
    clip1Display = Show(clip1, renderView1)

    # hide data in view
    Hide(clip2, renderView1)

    # hide data in view
    Hide(clip1, renderView1)

    # set active source
    SetActiveSource(clip2)

    # create a new 'Contour'
    contour2 = Contour(Input=clip2)
    contour2.ContourBy = ['POINTS', 'C_PSI4_REAL']
    contour2.Isosurfaces = [2e-06]
    contour2.PointMergeMethod = 'Uniform Binning'

    # show data in view
    contour2Display = Show(contour2, renderView1)
    # trace defaults for the display properties.
    contour2Display.Representation = 'Surface'
    contour2Display.ColorArrayName = [None, '']
    contour2Display.OSPRayScaleArray = 'C_HAM'
    contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour2Display.SelectOrientationVectors = 'C_HAM'
    contour2Display.ScaleFactor = 80.0
    contour2Display.SelectScaleArray = 'C_HAM'
    contour2Display.GlyphType = 'Arrow'
    contour2Display.GlyphTableIndexArray = 'C_HAM'
    contour2Display.DataAxesGrid = 'GridAxesRepresentation'
    contour2Display.PolarAxes = 'PolarAxesRepresentation'
    contour2Display.GaussianRadius = 40.0
    contour2Display.SetScaleArray = ['POINTS', 'C_HAM']
    contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour2Display.OpacityArray = ['POINTS', 'C_HAM']
    contour2Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(clip2, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice1)

    # Rescale transfer function
    c_PSI4_REALLUT.RescaleTransferFunction(-2e-05, 2e-05)

    # Rescale transfer function
    c_PSI4_REALPWF.RescaleTransferFunction(-2e-05, 2e-05)

    # set active source
    SetActiveSource(contour2)

    # change solid color
    contour2Display.DiffuseColor = [1.0, 0.0, 0.0]

    # set active source
    SetActiveSource(contour1)

    # change solid color
    contour1Display.DiffuseColor = [0.0, 0.0, 1.0]

    # get layout
    layout1 = GetLayout()

    # split cell
    layout1.SplitHorizontal(0, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'Render View'
    renderView2 = CreateView('RenderView')
    renderView2.ViewSize = [800, 800]
    renderView2.AxesGrid = 'GridAxes3DActor'
    renderView2.StereoType = 0
    renderView2.Background = [0.32, 0.34, 0.43]

    # place view in the layout
    layout1.AssignView(2, renderView2)

    # set active view
    SetActiveView(renderView1)

    # set active view
    SetActiveView(renderView2)

    # set active source
    SetActiveSource(clip2)

    # create a new 'Contour'
    contour3 = Contour(Input=clip2)
    contour3.ContourBy = ['POINTS', 'C_PSI4_IMG']
    contour3.Isosurfaces = [-2e-06]
    contour3.PointMergeMethod = 'Uniform Binning'

    # show data in view
    contour3Display = Show(contour3, renderView2)
    # trace defaults for the display properties.
    contour3Display.Representation = 'Surface'
    contour3Display.ColorArrayName = [None, '']
    contour3Display.OSPRayScaleArray = 'C_HAM'
    contour3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour3Display.SelectOrientationVectors = 'C_HAM'
    contour3Display.ScaleFactor = 80.0
    contour3Display.SelectScaleArray = 'C_HAM'
    contour3Display.GlyphType = 'Arrow'
    contour3Display.GlyphTableIndexArray = 'C_HAM'
    contour3Display.DataAxesGrid = 'GridAxesRepresentation'
    contour3Display.PolarAxes = 'PolarAxesRepresentation'
    contour3Display.GaussianRadius = 40.0
    contour3Display.SetScaleArray = ['POINTS', 'C_HAM']
    contour3Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour3Display.OpacityArray = ['POINTS', 'C_HAM']
    contour3Display.OpacityTransferFunction = 'PiecewiseFunction'

    # reset view to fit data
    renderView2.ResetCamera()

    # update the view to ensure updated data information
    renderView2.Update()

    # set active source
    SetActiveSource(clip2)

    # create a new 'Contour'
    contour4 = Contour(Input=clip2)
    contour4.ContourBy = ['POINTS', 'C_PSI4_IMG']
    contour4.Isosurfaces = [2e-06]
    contour4.PointMergeMethod = 'Uniform Binning'

    # show data in view
    contour4Display = Show(contour4, renderView2)
    # trace defaults for the display properties.
    contour4Display.Representation = 'Surface'
    contour4Display.ColorArrayName = [None, '']
    contour4Display.OSPRayScaleArray = 'C_HAM'
    contour4Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour4Display.SelectOrientationVectors = 'C_HAM'
    contour4Display.ScaleFactor = 80.0
    contour4Display.SelectScaleArray = 'C_HAM'
    contour4Display.GlyphType = 'Arrow'
    contour4Display.GlyphTableIndexArray = 'C_HAM'
    contour4Display.DataAxesGrid = 'GridAxesRepresentation'
    contour4Display.PolarAxes = 'PolarAxesRepresentation'
    contour4Display.GaussianRadius = 40.0
    contour4Display.SetScaleArray = ['POINTS', 'C_HAM']
    contour4Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour4Display.OpacityArray = ['POINTS', 'C_HAM']
    contour4Display.OpacityTransferFunction = 'PiecewiseFunction'

    # update the view to ensure updated data information
    renderView2.Update()

    # change solid color
    contour4Display.DiffuseColor = [1.0, 0.0, 0.0]

    # set active source
    SetActiveSource(contour3)

    # change solid color
    contour3Display.DiffuseColor = [0.0, 0.0, 1.0]

    # set active source
    SetActiveSource(bssn_gr_160000pvtu)

    # create a new 'Slice'
    slice2 = Slice(Input=bssn_gr_160000pvtu)
    slice2.SliceType = 'Plane'
    slice2.SliceOffsetValues = [0.0]

    # Properties modified on slice2.SliceType
    slice2.SliceType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    slice2Display = Show(slice2, renderView2)
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

    # update the view to ensure updated data information
    renderView2.Update()

    # set scalar coloring
    ColorBy(slice2Display, ('POINTS', 'C_PSI4_IMG'))

    # rescale color and/or opacity maps used to include current data range
    slice2Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    slice2Display.SetScalarBarVisibility(renderView2, True)

    # get color transfer function/color map for 'C_PSI4_IMG'
    c_PSI4_IMGLUT = GetColorTransferFunction('C_PSI4_IMG')

    # Rescale transfer function
    c_PSI4_IMGLUT.RescaleTransferFunction(-2e-05, 2e-05)

    # get opacity transfer function/opacity map for 'C_PSI4_IMG'
    c_PSI4_IMGPWF = GetOpacityTransferFunction('C_PSI4_IMG')

    # Rescale transfer function
    c_PSI4_IMGPWF.RescaleTransferFunction(-2e-05, 2e-05)

    # set active view
    SetActiveView(renderView1)

    # set active source
    SetActiveSource(bssn_gr_160000pvtu)

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1130.6691483706304, -1168.2524590970697, 199.50126142019948]
    renderView1.CameraFocalPoint = [4.274205465103137, -14.56100619247303, -38.89718424355462]
    renderView1.CameraViewUp = [0.09474942248980224, 0.11121266532949192, 0.9892695739828247]
    renderView1.CameraParallelScale = 630.4256130908655

    # current camera placement for renderView2
    renderView2.CameraPosition = [-1130.6691483706304, -1168.2524590970697, 199.50126142019948]
    renderView2.CameraFocalPoint = [4.274205465103137, -14.56100619247303, -38.89718424355462]
    renderView2.CameraViewUp = [0.09474942248980224, 0.11121266532949192, 0.9892695739828247]
    renderView2.CameraParallelScale = 630.4256130908655

    #### uncomment the following to render all views
    RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
    layout1 = GetLayout()
    
    SaveScreenshot(outFile, layout1, SaveAllViews=1, ImageResolution=[2400, 1200])
    
    Disconnect()
    Connect()
    
#filenameNumbers = [0, 50000, 80000]
framenumbers = [90000 + i*1000 for i in range(107)]
filenameNumbers = []
for n in framenumbers:
	filenameNumbers.append(n)

for fnum in filenameNumbers:
    infile = '/scratch/kingspeak/serial/u1011531/GR/q1_d15_R1.00_wtol_1e-4/vtu/bssn_gr_'+str(fnum)+'.pvtu'
    outfile = 'psi4split_'+str(fnum)+'.png'
    
    print('preparing to make '+str(fnum))
    make_mesh_image(infile, outfile)
    print('finished '+str(fnum))