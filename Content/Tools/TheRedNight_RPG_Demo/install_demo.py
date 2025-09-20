
# install_demo.py
# TheRedNight RPG Demo Installer
# Creates UI widgets, blueprint stubs, loot settings, and a demo map scaffold.
# NOTE: Complex Blueprint graph wiring across engine versions is fragile. This creates assets and
# folders reliably; then you can use AutoHUD actor/Level Blueprint to finalize runtime hookups in minutes.
import unreal

LOG="TRN Demo Installer:"
def log(m): unreal.log(f"{LOG} {m}")
def warn(m): unreal.log_warning(f"{LOG} {m}")
def err(m): unreal.log_error(f"{LOG} {m}")

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
ea = unreal.EditorAssetLibrary
eu = unreal.EditorUtilityLibrary

# Paths
UI_PATH = "/Game/UI"
BP_PATH = "/Game/Blueprints"
MAP_PATH = "/Game/Maps"
DATA_PATH = "/Game/Data"

def ensure_dir(path):
    if not ea.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)
        log(f"Created dir: {path}")
    else:
        log(f"Dir exists: {path}")

def create_widget(name):
    factory = unreal.WidgetBlueprintFactory()
    try:
        asset = asset_tools.create_asset(name, UI_PATH, unreal.WidgetBlueprint, factory)
        ea.save_asset(f"{UI_PATH}/{name}")
        log(f"Widget: {name} OK")
        return asset
    except Exception as e:
        err(f"Create widget failed {name}: {e}")
        return None

def create_actor_blueprint(name, parent=unreal.Actor):
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("ParentClass", parent)
    try:
        bp = asset_tools.create_asset(name, BP_PATH, unreal.Blueprint, factory)
        ea.save_asset(f"{BP_PATH}/{name}")
        log(f"Blueprint: {name} (parent={parent.get_name()}) OK")
        return bp
    except Exception as e:
        err(f"Create BP failed {name}: {e}")
        return None

def create_data_asset(name, cls):
    factory = unreal.DataAssetFactory()
    factory.set_editor_property("DataAssetClass", cls)
    try:
        da = asset_tools.create_asset(name, DATA_PATH, unreal.DataAsset, factory)
        ea.save_asset(f"{DATA_PATH}/{name}")
        log(f"DataAsset: {name} ({cls.get_name()}) OK")
        return da
    except Exception as e:
        err(f"Create DataAsset failed {name}: {e}")
        return None

def main():
    log("Start")
    for p in (UI_PATH, BP_PATH, MAP_PATH, DATA_PATH):
        ensure_dir(p)

    # UI
    w_hud  = create_widget("WBP_HUD")
    w_hp   = create_widget("WBP_HealthBar")
    w_mp   = create_widget("WBP_ManaBar")
    w_toast= create_widget("WBP_LootToast")

    # BP Stubs
    bp_autohud   = create_actor_blueprint("BP_AutoHUD", unreal.Actor)
    bp_chest     = create_actor_blueprint("BP_LootChest", unreal.Actor)
    bp_enemy     = create_actor_blueprint("BP_Enemy_Trash", unreal.Character)

    # Data (placeholder; user will edit on BP_LootChest Details later)
    # You can later replace with a real DataTable; for now we just provide the container folder
    # and recommend setting arrays on BP_LootChest (LootNames, RarityWeights) manually.
    # This keeps version-compat solid.
    log("Scaffold created. Open Blueprints to finalize small graphs if needed.")

    # Map scaffold (create an empty level named Map_LootDemo)
    world_factory = unreal.WorldFactory()
    try:
        map_asset = asset_tools.create_asset("Map_LootDemo", MAP_PATH, unreal.World, world_factory)
        ea.save_asset(f"{MAP_PATH}/Map_LootDemo")
        log("Map_LootDemo created.")
    except Exception as e:
        warn(f"Could not create map asset automatically: {e}")

    # Finalize
    for d in (UI_PATH, BP_PATH, MAP_PATH, DATA_PATH):
        ea.save_directory(d, only_if_is_dirty=False, recursive=True)
        try:
            unreal.EditorAssetLibrary.fixup_redirectors(d)
        except Exception:
            pass

    log("DONE")

if __name__ == "__main__":
    main()
