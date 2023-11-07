def calculate_distance_to_cones(cones):
    CONE_HEIGHT_CONSTANT = 100  # Substitua este valor pelo desejado

    for cone in cones:
        bounding_rect = cone.boxes  # Substitua pela bounding box fornecida pelo algoritmo de ML

        distance = CONE_HEIGHT_CONSTANT / bounding_rect[3]
        cones['landmarks'].append({'color': color, 'distance': distance, 0: 0, 'bounding_box': bounding_rect})
