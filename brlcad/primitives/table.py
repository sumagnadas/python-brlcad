"""
Maps the BRL-CAD primitive type codes to the python wrapper classes.
"""
import warnings

import brlcad.bindings.raytrace as rt
from brlcad.bindings import bu
from brlcad.exceptions import BRLCADException
from .arb8 import ARB8
from .arbn import ARBN
from .base import Primitive
from .ellipsoid import Ellipsoid, Sphere
from .rpc import RPC, RHC
#from vol import VOL
#from ars import ARS
#from half import Half
#from tgc import TGC
#from torus import Torus, ETO
#from epa import EPA, EHY
from .combination import Combination
#from hyperboloid import Hyperboloid
#from particle import Particle
#from pipe import Pipe
#from sketch import Sketch, Extrude, Revolve
#from superell import Superell
#from metaball import Metaball
#from ebm import EBM
#from grip import Grip
#from bot import BOT
#from submodel import Submodel


MAGIC_TO_PRIMITIVE_TYPE = {
    # TODO: add proper wrappers for all primitives which have here "Primitive" as wrapper
    rt.ID_ARBN: ("ARBN", ARBN, rt.RT_ARBN_INTERNAL_MAGIC, rt.struct_rt_arbn_internal),
    rt.ID_ARB8: ("ARB", ARB8, bu.RT_ARB_INTERNAL_MAGIC, rt.struct_rt_arb_internal),
    rt.ID_BINUNIF: ("BINUNIF", Primitive, bu.RT_BINUNIF_INTERNAL_MAGIC, rt.struct_rt_binunif_internal),
    #rt.ID_BOT: ("BOT", BOT, bu.RT_BOT_INTERNAL_MAGIC, rt.struct_rt_bot_internal),
    rt.ID_BREP: ("BREP", Primitive, bu.RT_BREP_INTERNAL_MAGIC, rt.struct_rt_brep_internal),
    rt.ID_CLINE: ("CLINE", Primitive, bu.RT_CLINE_INTERNAL_MAGIC, rt.struct_rt_cline_internal),
    rt.ID_DSP: ("DSP", Primitive, bu.RT_DSP_INTERNAL_MAGIC, rt.struct_rt_dsp_internal),
    #rt.ID_EBM: ("EBM", EBM, rt.RT_EBM_INTERNAL_MAGIC, rt.struct_rt_ebm_internal),
    #rt.ID_EHY: ("EHY", EHY, rt.RT_EHY_INTERNAL_MAGIC, rt.struct_rt_ehy_internal),
    rt.ID_ELL: ("ELL", Ellipsoid, bu.RT_ELL_INTERNAL_MAGIC, rt.struct_rt_ell_internal),
    rt.ID_SPH: ("ELL", Sphere, bu.RT_ELL_INTERNAL_MAGIC, rt.struct_rt_ell_internal),
    #rt.ID_EPA: ("EPA", EPA, rt.RT_EPA_INTERNAL_MAGIC, rt.struct_rt_epa_internal),
    #rt.ID_ETO: ("ETO", ETO, rt.RT_ETO_INTERNAL_MAGIC, rt.struct_rt_eto_internal),
    #rt.ID_EXTRUDE: ("EXTRUDE", Extrude, rt.RT_EXTRUDE_INTERNAL_MAGIC, rt.struct_rt_extrude_internal),
    #rt.ID_GRIP: ("GRIP", Grip, rt.RT_GRIP_INTERNAL_MAGIC, rt.struct_rt_grip_internal),
    #rt.ID_HALF: ("HALF", Half, rt.RT_HALF_INTERNAL_MAGIC, rt.struct_rt_half_internal),
    rt.ID_HF: ("HF", Primitive, bu.RT_HF_INTERNAL_MAGIC, rt.struct_rt_hf_internal),
    #rt.ID_HYP: ("HYP", Hyperboloid, rt.RT_HYP_INTERNAL_MAGIC, rt.struct_rt_hyp_internal),
    #rt.ID_METABALL: ("METABALL", Metaball, rt.RT_METABALL_INTERNAL_MAGIC, rt.struct_rt_metaball_internal),
    rt.ID_BSPLINE: ("NURB", Primitive, bu.RT_NURB_INTERNAL_MAGIC, rt.struct_rt_nurb_internal),
    rt.ID_POLY: ("PG", Primitive, bu.RT_PG_INTERNAL_MAGIC, rt.struct_rt_pg_internal),
    #rt.ID_PIPE: ("PIPE", Pipe, rt.RT_PIPE_INTERNAL_MAGIC, rt.struct_rt_pipe_internal),
    #rt.ID_PARTICLE: ("PARTICLE", Particle, rt.RT_PART_INTERNAL_MAGIC, rt.struct_rt_part_internal),
    #rt.ID_REVOLVE: ("REVOLVE", Revolve, rt.RT_REVOLVE_INTERNAL_MAGIC, rt.struct_rt_revolve_internal),
    rt.ID_RHC: ("RHC", RHC, rt.RT_RHC_INTERNAL_MAGIC, rt.struct_rt_rhc_internal),
    rt.ID_RPC: ("RPC", RPC, rt.RT_RPC_INTERNAL_MAGIC, rt.struct_rt_rpc_internal),
    #rt.ID_SKETCH: ("SKETCH", Sketch, rt.RT_SKETCH_INTERNAL_MAGIC, rt.struct_rt_sketch_internal),
    #rt.ID_SUBMODEL: ("SUBMODEL", Submodel, rt.RT_SUBMODEL_INTERNAL_MAGIC, rt.struct_rt_submodel_internal),
    #rt.ID_SUPERELL: ("SUPERELL", Superell, rt.RT_SUPERELL_INTERNAL_MAGIC, rt.struct_rt_superell_internal),
    #rt.ID_TGC: ("TGC", TGC, rt.RT_TGC_INTERNAL_MAGIC, rt.struct_rt_tgc_internal),
    #rt.ID_REC: ("REC", TGC, rt.RT_TGC_INTERNAL_MAGIC, rt.struct_rt_tgc_internal),
    #rt.ID_TOR: ("TOR", Torus, rt.RT_TOR_INTERNAL_MAGIC, rt.struct_rt_tor_internal),
    #rt.ID_VOL: ("VOL", VOL, rt.RT_VOL_INTERNAL_MAGIC, rt.struct_rt_vol_internal),
    #rt.ID_ARS: ("ARS", ARS, rt.RT_ARS_INTERNAL_MAGIC, rt.struct_rt_ars_internal),
    rt.ID_PNTS: ("PNTS", Primitive, bu.RT_PNTS_INTERNAL_MAGIC, rt.struct_rt_pnts_internal),
    rt.ID_ANNOT: ("ANNOTATION", Primitive, bu.RT_ANNOT_INTERNAL_MAGIC, rt.struct_rt_annot_internal),
    rt.ID_COMBINATION: ("COMBINATION", Combination, rt.RT_COMB_MAGIC, rt.struct_rt_comb_internal),
    rt.ID_CONSTRAINT: ("CONSTRAINT", Primitive, bu.RT_CONSTRAINT_MAGIC, rt.struct_rt_constraint_internal),
}

def create_primitive(type_id, db_internal, directory):
    # TODO: research if this method won't cause a memory leak
    name = str(directory.d_namep)
    type_info = MAGIC_TO_PRIMITIVE_TYPE.get(type_id)
    if type_info:
        magic = type_info[2]
        struct_type = type_info[3]
        data = struct_type.from_address(db_internal.idb_ptr) if struct_type else None
        # the first int32 is always the magic:
        data_magic = rt.cast(db_internal.idb_ptr, rt.POINTER(rt.c_uint32)).contents.value
        if magic:
            if magic != data_magic:
                raise BRLCADException("Invalid magic value, expected {0} but got {1}".format(magic, data_magic))
        else:
            if type_info[2]:
                display_type_info = list(type_info)
                display_type_info[2] = hex(display_type_info[2])
            else:
                display_type_info = type_info
            warnings.warn("No magic for type: {0}, {1}, {2}".format(type_id, hex(data_magic), display_type_info))
        if type_info[1] == Primitive:
            return Primitive(name=name, primitive_type=type_info[0], data=data)
        else:
            return type_info[1].from_wdb(name=name, data=data)
    else:
        return Primitive(name=name, primitive_type="UNKNOWN")
