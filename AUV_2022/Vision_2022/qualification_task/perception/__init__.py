import perception.vis.TestAlgo as TestAlgo
import perception.tasks.gate.GateCenterAlgo as GateSeg
import perception.tasks.gate.GateSegmentationAlgoA as GateSegA
import perception.tasks.segmentation.saliency_detection.MBD as MBD
from perception.tasks.segmentation.COMB_SAL_BG import COMB_SAL_BG
import perception.vis.TestTasks.BackgroundRemoval as BackgroundRemoval

ALGOS = {
    'test': TestAlgo.TestAlgo,
    'gateseg': GateSeg.GateCenterAlgo,
    'gatesegA': GateSegA.GateSegmentationAlgoA,
    'MBD': MBD.MBD,
    'bg-rm': BackgroundRemoval.BackgroundRemoval,
    'combined': COMB_SAL_BG
}
