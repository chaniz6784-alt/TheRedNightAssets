
# create_widgets.py
# Unreal Editor Python script to programmatically create simple Widget Blueprints:
# WBP_HUD, WBP_HealthBar, WBP_ManaBar, WBP_LootToast
#
# Run this from the Unreal Editor Python console:
# exec(open(r"C:\full\path\to\create_widgets.py").read())

import unreal

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

PACKAGE_PATH = "/Game/UI"

def ensure_folder(path):
    if not editor_asset_lib.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)

def create_widget_blueprint(name):
    factory = unreal.WidgetBlueprintFactory()
    try:
        asset = asset_tools.create_asset(name, PACKAGE_PATH, unreal.WidgetBlueprint, factory)
        saved = editor_asset_lib.save_asset(PACKAGE_PATH + "/" + name)
        unreal.log("Created and saved: {}/{} -> {}".format(PACKAGE_PATH, name, saved))
        return asset
    except Exception as e:
        unreal.log_error("Failed to create {}: {}".format(name, e))
        return None

def add_simple_healthbar(widget_bp):
    # Try to modify the UMG blueprint's designer tree if possible.
    # This is a best-effort: complex UMG editing via Python can be limited across engine versions.
    unreal.log("You can open the widget in the editor to refine layout: {}".format(widget_bp.get_path_name()))

def main():
    ensure_folder(PACKAGE_PATH)
    names = ["WBP_HUD", "WBP_HealthBar", "WBP_ManaBar", "WBP_LootToast"]
    created = {}
    for n in names:
        created[n] = create_widget_blueprint(n)

    unreal.log("WBP_HUD_Package: creation complete. Open Content Browser -> /Game/UI to view assets.")
    unreal.log("If widgets are empty or need layout changes, open each widget and add ProgressBar/Text/Images as needed.")
    unreal.log("To auto-display WBP_HUD at runtime: In your PlayerController BeginPlay -> Create Widget (WBP_HUD) -> Add to Viewport.")
    return created

if __name__ == "__main__":
    main()
