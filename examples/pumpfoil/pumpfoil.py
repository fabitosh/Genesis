import genesis as gs

SCENE_WIDTH_M = 1.0

gs.init(backend=gs.metal, precision="32")

res = 384
scene = gs.Scene(
    sim_options=gs.options.SimOptions(
        dt=0.01,
        substeps=1,  # substep_dt = dt/n_substeps
    ),
    sph_options=gs.options.SPHOptions(  # lagrangian solver
        # area where the simulation takes place
        lower_bound=(-SCENE_WIDTH_M / 2, -SCENE_WIDTH_M / 2, 0.0),
        upper_bound=(SCENE_WIDTH_M / 2, SCENE_WIDTH_M / 2, 1.0),
        particle_size=0.04,  # particle size in [meters]
    ),
    vis_options=gs.options.VisOptions(
        visualize_sph_boundary=True,
    ),
    viewer_options=gs.options.ViewerOptions(
        res=(res, res)
    ),
    show_viewer=True)
plane = scene.add_entity(gs.morphs.Plane())
water = scene.add_entity(
    material=gs.materials.SPH.Liquid(
        sampler='pbs'
    ),
    morph=gs.morphs.Box(
        pos=(0.0, 0.0, 0.2),
        size=(SCENE_WIDTH_M, SCENE_WIDTH_M, 0.4),
    ),
    surface=gs.surfaces.Water(
        # color=(0.4, 0.8, 1.0),
        vis_mode='particle',
    ),
)
# todo: does not seem to be shown
foil = scene.add_entity(
    gs.morphs.Mesh(
        file="assets/beta_2_pump_foil_monster.stl",
        pos=(0.0, 0.0, 0.3),
        scale=0.5,
    )
)
scene.build()
for i in range(1000):
    scene.step()
