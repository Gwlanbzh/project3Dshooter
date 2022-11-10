{ pkgs ? import <nixpkgs> {} }:
with pkgs;
mkShell {
  buildInputs = [
    python310Packages.pygame # Nixpkgs fixes up some complexities
    vulkan-loader # Griddly needs the Vulkan-SDK
  ];
  LD_LIBRARY_PATH="${vulkan-loader}/lib";
}