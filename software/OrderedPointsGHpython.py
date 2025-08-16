ordered_points = []

for i, crv in enumerate(curves):
    # Get curve length and divide it
    length = crv.GetLength()
    div_count = max(int(length / segment_length), 1)
    t_vals = [j / float(div_count) for j in range(div_count + 1)]
    pts = [crv.PointAt(crv.Domain.ParameterAt(t)) for t in t_vals]

    # Get start and end points
    start_pt = crv.PointAtStart
    end_pt = crv.PointAtEnd

    if i == 0:
        # Add first curve points directly
        ordered_points.extend(pts)
    else:
        # Offset end of previous curve
        end_offset = Point3d(prev_end_pt.X, prev_end_pt.Y, prev_end_pt.Z + z_offset)
        ordered_points.append(end_offset)

        # Offset start of current curve
        start_offset = Point3d(start_pt.X, start_pt.Y, start_pt.Z + z_offset)
        ordered_points.append(start_offset)

        # Add curve points
        ordered_points.extend(pts)

    # Always update for next loop
    prev_end_pt = end_pt

# Output
a = ordered_points
