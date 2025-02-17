// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.29.3
// source: location.proto

package location

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	LocationService_GetUserLocation_FullMethodName   = "/location.LocationService/getUserLocation"
	LocationService_GetDriverLocation_FullMethodName = "/location.LocationService/getDriverLocation"
	LocationService_UpdateLocation_FullMethodName    = "/location.LocationService/updateLocation"
)

// LocationServiceClient is the client API for LocationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type LocationServiceClient interface {
	GetUserLocation(ctx context.Context, in *GetUserLocationRequest, opts ...grpc.CallOption) (*Location, error)
	GetDriverLocation(ctx context.Context, in *GetDriverLocationRequest, opts ...grpc.CallOption) (*Location, error)
	UpdateLocation(ctx context.Context, in *UpdateLocationRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type locationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewLocationServiceClient(cc grpc.ClientConnInterface) LocationServiceClient {
	return &locationServiceClient{cc}
}

func (c *locationServiceClient) GetUserLocation(ctx context.Context, in *GetUserLocationRequest, opts ...grpc.CallOption) (*Location, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Location)
	err := c.cc.Invoke(ctx, LocationService_GetUserLocation_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *locationServiceClient) GetDriverLocation(ctx context.Context, in *GetDriverLocationRequest, opts ...grpc.CallOption) (*Location, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Location)
	err := c.cc.Invoke(ctx, LocationService_GetDriverLocation_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *locationServiceClient) UpdateLocation(ctx context.Context, in *UpdateLocationRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, LocationService_UpdateLocation_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// LocationServiceServer is the server API for LocationService service.
// All implementations must embed UnimplementedLocationServiceServer
// for forward compatibility.
type LocationServiceServer interface {
	GetUserLocation(context.Context, *GetUserLocationRequest) (*Location, error)
	GetDriverLocation(context.Context, *GetDriverLocationRequest) (*Location, error)
	UpdateLocation(context.Context, *UpdateLocationRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedLocationServiceServer()
}

// UnimplementedLocationServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedLocationServiceServer struct{}

func (UnimplementedLocationServiceServer) GetUserLocation(context.Context, *GetUserLocationRequest) (*Location, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetUserLocation not implemented")
}
func (UnimplementedLocationServiceServer) GetDriverLocation(context.Context, *GetDriverLocationRequest) (*Location, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDriverLocation not implemented")
}
func (UnimplementedLocationServiceServer) UpdateLocation(context.Context, *UpdateLocationRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateLocation not implemented")
}
func (UnimplementedLocationServiceServer) mustEmbedUnimplementedLocationServiceServer() {}
func (UnimplementedLocationServiceServer) testEmbeddedByValue()                         {}

// UnsafeLocationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to LocationServiceServer will
// result in compilation errors.
type UnsafeLocationServiceServer interface {
	mustEmbedUnimplementedLocationServiceServer()
}

func RegisterLocationServiceServer(s grpc.ServiceRegistrar, srv LocationServiceServer) {
	// If the following call pancis, it indicates UnimplementedLocationServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&LocationService_ServiceDesc, srv)
}

func _LocationService_GetUserLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetUserLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LocationServiceServer).GetUserLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: LocationService_GetUserLocation_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LocationServiceServer).GetUserLocation(ctx, req.(*GetUserLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _LocationService_GetDriverLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetDriverLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LocationServiceServer).GetDriverLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: LocationService_GetDriverLocation_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LocationServiceServer).GetDriverLocation(ctx, req.(*GetDriverLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _LocationService_UpdateLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LocationServiceServer).UpdateLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: LocationService_UpdateLocation_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LocationServiceServer).UpdateLocation(ctx, req.(*UpdateLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// LocationService_ServiceDesc is the grpc.ServiceDesc for LocationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var LocationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "location.LocationService",
	HandlerType: (*LocationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "getUserLocation",
			Handler:    _LocationService_GetUserLocation_Handler,
		},
		{
			MethodName: "getDriverLocation",
			Handler:    _LocationService_GetDriverLocation_Handler,
		},
		{
			MethodName: "updateLocation",
			Handler:    _LocationService_UpdateLocation_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "location.proto",
}
