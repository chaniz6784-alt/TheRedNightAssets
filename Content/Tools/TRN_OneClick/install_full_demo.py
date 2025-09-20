
import unreal

LOG = "TRN OneClick:"
def log(x): unreal.log(f"{LOG} {x}")
def warn(x): unreal.log_warning(f"{LOG} {x}")

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
EA = unreal.EditorAssetLibrary
EL = unreal.EditorLevelLibrary

UI_PATH = "/Game/UI"
BP_PATH = "/Game/Blueprints"
MAP_PATH = "/Game/Maps"

def ensure_dir(path):
    if not EA.does_directory_exist(path):
        EA.make_directory(path); log(f"Dir created: {path}")
    else:
        log(f"Dir exists: {path}")

def create_widget(name):
    f = unreal.WidgetBlueprintFactory()
    a = asset_tools.create_asset(name, UI_PATH, unreal.WidgetBlueprint, f)
    EA.save_asset(f"{UI_PATH}/{name}")
    log(f"Widget OK: {name}")

def create_bp(name, parent):
    f = unreal.BlueprintFactory(); f.set_editor_property("ParentClass", parent)
    a = asset_tools.create_asset(name, BP_PATH, unreal.Blueprint, f)
    EA.save_asset(f"{BP_PATH}/{name}")
    log(f"BP OK: {name} (parent {parent.get_name()})")

def create_map(name):
    wf = unreal.WorldFactory()
    a = asset_tools.create_asset(name, MAP_PATH, unreal.World, wf)
    EA.save_asset(f"{MAP_PATH}/{name}")
    log(f"Map OK: {name}")

def main():
    for p in (UI_PATH, BP_PATH, MAP_PATH): ensure_dir(p)
    for w in ("WBP_HUD","WBP_HealthBar","WBP_ManaBar","WBP_LootToast"):
        if not EA.does_asset_exist(f"{UI_PATH}/{w}"): create_widget(w)
    if not EA.does_asset_exist(f"{BP_PATH}/BP_AutoHUD"):  create_bp("BP_AutoHUD", unreal.Actor)
    if not EA.does_asset_exist(f"{BP_PATH}/BP_LootChest"):create_bp("BP_LootChest", unreal.Actor)
    if not EA.does_asset_exist(f"{BP_PATH}/BP_Enemy_Trash"):create_bp("BP_Enemy_Trash", unreal.Character)
    if not EA.does_asset_exist(f"{MAP_PATH}/Map_LootDemo"):create_map("Map_LootDemo")
    try:
        EL.load_level("/Game/Maps/Map_LootDemo")
        log("Loaded Map_LootDemo")
        # Place stubs so you can see them in the map right away
        def spawn(class_path, loc):
            try:
                cls = EA.load_asset(class_path)
                EL.spawn_actor_from_class(cls, unreal.Vector(*loc), unreal.Rotator(0,0,0))
                log(f"Spawned {class_path} at {loc}")
            except Exception as e: warn(f"Spawn failed {class_path}: {e}")
        spawn("/Game/Blueprints/BP_AutoHUD", (0,0,100))
        spawn("/Game/Blueprints/BP_LootChest", (300,0,90))
        spawn("/Game/Blueprints/BP_Enemy_Trash", (-400,200,90))
        EL.save_current_level(); log("Saved Map_LootDemo with placed actors.")
    except Exception as e:
        warn(f"Could not load level to place actors: {e}")
    for p in (UI_PATH, BP_PATH, MAP_PATH):
        EA.save_directory(p, only_if_is_dirty=False, recursive=True)
        try: unreal.EditorAssetLibrary.fixup_redirectors(p)
        except Exception: pass
    log("DONE")

if __name__ == "__main__":
    main()
