#ifndef SPHERE_H
#define SPHERE_H

#include "rtweekend.h"
#include "hittable.h"

class sphere : public hittable 
{
public : 
    sphere (const point3& center , double radius ,shared_ptr<material> mat ) : center(center), radius(std::fmax(0,radius)), mat(mat)
    {
        auto rvec = vec3(radius, radius, radius);
        bbox = aabb(center - rvec, center + rvec);
    }


    bool hit(const ray& r , interval ray_t , hit_record& rec) const override
    {
        vec3 oc = center - r.origin();
        double a = dot(r.direction() , r.direction());
        double h = dot(r.direction() , oc);
        double c = dot(oc, oc) - radius*radius ; 
        auto discriminant = h*h - a*c ;

        if(discriminant < 0.0 ) return false;
        
        auto sqrtd = std::sqrt(discriminant) ; 

        // Find the nearest root that lies in the acceptable range.

        auto root = (h - sqrtd) / a ;
        if(!ray_t.contains(root)) 
        {
            root = (h + sqrtd) /a ;
            if(!ray_t.contains(root)) return false ;
        }

        rec.t = root ;
        rec.p = r.at(root);
        vec3 outward_normal = (rec.p - center) / radius ; 
        rec.set_face_normal(r,outward_normal);
        rec.mat = mat;

        return true ; 
    }

    aabb bounding_box() const override { return bbox; }


private : 

    point3 center ; 
    double radius ; 
    shared_ptr<material> mat;
    aabb bbox;

};

#endif
