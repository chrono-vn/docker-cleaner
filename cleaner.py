#!/usr/bin/env python3
"""
docker-cleaner - A tool to clean up unused Docker resources.
"""
import docker
import argparse

# Connect to docker daemon using the default socket
client = docker.from_env()

def list_unused_containers():
	"""Lists stopped containers."""
	stopped_containers = client.containers.list(all=True, filters={"status":"exited"})
	return stopped_containers

def list_dangling_images():
	"""Lists Dangling images (layers with no tags)."""
	dangling_images = client.images.list(filters={"dangling": True})
	return dangling_images

def list_unused_volumes():
	"""Lists unused volumes (not mounted by any container)."""
	volumes = client.volumes.list(filters={"dangling": True})
	return volumes


def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Clean up unused Docker resources.")
    parser.add_argument('--dry-run', action='store_true', help="List resources but don't delete them.")
    parser.add_argument('--containers', action='store_true', help="Target stopped containers.")
    parser.add_argument('--images', action='store_true', help="Target dangling images.")
    parser.add_argument('--volumes', action='store_true', help="Target unused volumes.")
    parser.add_argument('--all', action='store_true', help="Target all resource types.")

    args = parser.parse_args()

    # If no specific target is given, default to a dry-run of everything
    if not (args.containers or args.images or args.volumes):
        args.all = True
        args.dry_run = True
        print("INFO: No targets specified. Performing a dry-run of all resources. Use --help for options.\n")

    if args.all:
        args.containers = True
        args.images = True
        args.volumes = True

    print(f"DRY-RUN: {args.dry_run}")
    print("="*50)

    # Logic for containers
    if args.containers:
        containers = list_unused_containers()
        print(f"\nFound {len(containers)} stopped containers:")
        for container in containers:
            print(f"  - {container.name} ({container.id[:12]})")
            if not args.dry_run:
                container.remove() # This is the line that deletes it
                print(f"    Deleted.")

    if args.images:
        images = list_dangling_images()
        print(f"\nFound {len(images)} dangling images:")
        for image in images:
            print(f"  - {image.name} ({image.id[:12]})")
            if not args.dry_run:
                client.images.remove(image.id) # This is the line that deletes it
                print(f"    Deleted.")

    if args.volumes:
        volumes = list_unused_volumes()
        print(f"\nFound {len(volumes)} unused volumes:")
        for volume in volumes:
            print(f"  - {volume.name} ({volume.id[:12]})")
            if not args.dry_run:
                volume.remove() # This is the line that deletes it
                print(f"    Deleted.")

    # ... (Add similar logic blocks for 'images' and 'volumes' here)
    # This is your task! Use the containers block as a template.

if __name__ == "__main__":
    main()
