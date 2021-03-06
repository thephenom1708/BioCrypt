// Part of SourceAFIS for Java: https://sourceafis.machinezoo.com/java
package com.machinezoo.sourceafis;

import java.nio.*;

class BooleanMatrix {
	final int width;
	final int height;
	private final boolean[] array;
	BooleanMatrix(int width, int height) {
		this.width = width;
		this.height = height;
		array = new boolean[width * height];
	}
	BooleanMatrix(IntPoint size) {
		this(size.x, size.y);
	}
	BooleanMatrix(BooleanMatrix other) {
		this(other.size());
		for (int i = 0; i < array.length; ++i)
			array[i] = other.array[i];
	}
	IntPoint size() {
		return new IntPoint(width, height);
	}
	boolean get(int x, int y) {
		return array[offset(x, y)];
	}
	boolean get(IntPoint at) {
		return get(at.x, at.y);
	}
	boolean get(int x, int y, boolean fallback) {
		if (x < 0 || y < 0 || x >= width || y >= height)
			return fallback;
		return array[offset(x, y)];
	}
	boolean get(IntPoint at, boolean fallback) {
		return get(at.x, at.y, fallback);
	}
	void set(int x, int y, boolean value) {
		array[offset(x, y)] = value;
	}
	void set(IntPoint at, boolean value) {
		set(at.x, at.y, value);
	}
	void invert() {
		for (int i = 0; i < array.length; ++i)
			array[i] = !array[i];
	}
	void merge(BooleanMatrix other) {
		if (other.width != width || other.height != height)
			throw new IllegalArgumentException();
		for (int i = 0; i < array.length; ++i)
			array[i] |= other.array[i];
	}
	byte[] serialize() {
		ByteBuffer buffer = ByteBuffer.allocate(size().area());
		for (IntPoint at : size())
			buffer.put((byte)(get(at) ? 1 : 0));
		return buffer.array();
	}
	JsonArrayInfo json() {
		JsonArrayInfo info = new JsonArrayInfo();
		info.axes = new String[] { "y", "x" };
		info.dimensions = new int[] { height, width };
		info.scalar = "boolean";
		info.bitness = 8;
		info.format = "false as 0, true as 1";
		return info;
	}
	private int offset(int x, int y) {
		return y * width + x;
	}
}
